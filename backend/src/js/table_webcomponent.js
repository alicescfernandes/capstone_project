const API_BASE_URL = `${window.location.origin}/api/`;
class DataTableComponent extends HTMLElement {
    constructor() {
        super();
        this.initState();
        this.id = `table_${this.state.chartSlug}`;
        this.table = null;
        this.zoomTable = null;
    }

    initState() {
        this.state = {
            chartSlug: this.getAttribute("chart_slug"),
            quarterNumber: this.getAttribute("q"),
            data: [],
            columns: [],
            isError: false,
            isLoading: true,
            quarter: {
                current: "1",
                prev: null,
                next: null
            },
            dataTableSettings: {
                responsive: true,
                searching: true,
                ordering: true,
                paging: true,
                destroy: true, // Allow reinitialization
                debug: false, // Disable debug warnings
                pageLength: 5,
                lengthChange: false,
                search: {
                    smart: false,
                    caseInsensitive: true
                },
                searchCols: [], // Will be populated with columns when table is initialized
                language: {
                    search: "Search table:"
                }
            }
        };
    }

    static get observedAttributes() {
        return ['chart_slug', 'q'];
    }

    connectedCallback() {
        this.setupLazyLoad();
    }

    async fetchData() {
        const params = new URLSearchParams({
            slug: this.state.chartSlug,
            q: this.state.quarterNumber,
        });

        try {
            const res = await fetch(`${API_BASE_URL}chart/?${params.toString()}`);
            if (!res.ok) throw new Error(`HTTP error! Status: ${res.status}`);
            const data = await res.json();

            const { selected_option, ...rest } = data;

            this.setState({
                selectedOption: selected_option || "",
                ...rest
            });
        } catch {
            this.setState({ isError: true });
        } finally {
            this.setState({ isLoading: false });
        }
    }

    setState(newState) {
        this.state = { ...this.state, ...newState };
        this.render();
    }

    renderSpinner() {
        return `<div class="spinner-container" role="status">
            <svg aria-hidden="true" class="spinner-svg" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
            </svg>
            <span class="sr-only">Loading...</span>
        </div>`;
    }

    renderError() {
        return `
            <div class="alert-error" role="alert">
                <svg class="alert-error-svg" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
                </svg>
                <span class="sr-only">Info</span>
                <div>
                    <span class="font-bold">Unable to load table data.</span> Please try again later.
                </div>
            </div>
        `;
    }

    render() {
        if (this.state.isLoading) {
            this.innerHTML = this.renderSpinner();
            return;
        }
        if (this.state.isError) {
            this.innerHTML = this.renderError();
            return;
        }

        const newHTML = `
            <div class="chart-container">
                <div class="chart-header">
                    <h3 class="chart-title">${this.state.title} - Q${this.state.quarter.current}</h3>
                    <div class="chart-quarter-navigation">${this.renderQuarterNavigation()}</div>
                </div>
                ${this.renderZoomOverlay()}
                <div class="table-container" style="width:100%;height:400px;">
                    <table class="display responsive nowrap" style="width:100%"></table>
                </div>
            </div>`;

        this.innerHTML = newHTML;
        this.initializeTable();
        this.setupEvents();
        this.renderQuarterNavigation();
    }

    renderQuarterNavigation() {
        const { quarter, title } = this.state;

        return `
            <button aria-label="Zoom ${title} Chart" class="chart-quarter-nav-btn chart-zoom-btn"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H4m0 0v4m0-4 5 5m7-5h4m0 0v4m0-4-5 5M8 20H4m0 0v-4m0 4 5-5m7 5h4m0 0v-4m0 4-5-5"/></svg></button>
            <button aria-label="Navigate to Q${quarter?.prev}" ${!quarter?.prev ? 'disabled' : ''} class="prev-quarter chart-quarter-nav-btn"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12l4-4m-4 4 4 4"/></svg></button>
            <button aria-label="Navigate to Q${quarter?.next}" ${!quarter?.next ? 'disabled' : ''} class="next-quarter chart-quarter-nav-btn"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 12H5m14 0-4 4m4-4-4-4"/></svg></button>`;
    }

    renderZoomOverlay() {
        return `
            <div class="chart-zoom-overlay">
                <div class="chart-zoom-content">
                    <button class="chart-quarter-nav-btn chart-zoom-close"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 9h4m0 0V5m0 4L4 4m15 5h-4m0 0V5m0 4 5-5M5 15h4m0 0v4m0-4-5 5m15-5h-4m0 0v4m0-4 5 5"/>
                    </svg></button>
                    <div class="chart-zoom-container" style="padding-top:20px;width:100%; height:100%;">
                        <table class="display responsive nowrap" style="width:100%">
                        </table>
                    </div>
                </div>
            </div>
        `;
    }

    waitForDataTables() {
        if (window.DataTable) {
            return Promise.resolve();
        }

        if (window.isDataTableLoading) {
            return new Promise((resolve) => {
                const checkLoaded = () => {
                    if (window.isDataTableLoaded) {
                        resolve();
                    } else {
                        setTimeout(checkLoaded, 100);
                    }
                };
                checkLoaded();
            });
        }

        window.isDataTableLoading = true;
        return import(window.datatablesUrl).then(() => {
            window.isDataTableLoaded = true;
            window.isDataTableLoading = false;
            return Promise.resolve();
        });
    }

    async initializeTable() {
        // Don't initialize if table already exists
        if (this.table) {
            return;
        }

        await this.waitForDataTables();

        // Check if the table element exists
        const tableElement = this.querySelector(`table`);
        if (!tableElement) {
            return;
        }

        // Check if DataTable is already initialized on this element
        if ($.fn.DataTable.isDataTable(tableElement)) {
            return;
        }

        this.table = new DataTable(`table`, {
            data: this.state.data,
            columns: this.state.columns,
            ...this.state.dataTableSettings
        });
    }

    setupEvents() {
        // Quarter navigation events
        this.querySelector(`.prev-quarter`)?.addEventListener('click', () => this.handleQuarterChange('prev'));
        this.querySelector(`.next-quarter`)?.addEventListener('click', () => this.handleQuarterChange('next'));

        // Zoom functionality - Wait for next tick to ensure DOM is updated
        const zoomBtn = this.querySelector(`.chart-zoom-btn`);
        const zoomOverlay = this.querySelector(`.chart-zoom-overlay`);
        const zoomContent = this.querySelector(`.chart-zoom-container`);
        const closeZoom = this.querySelector(`.chart-zoom-close`);

        // Datatable uses jQuery so its easier to write logic for datatable with jQuery
        const showAllTextFilter = (node) => {
            $(node).on('click', function (e) {
                // Wait for the dropdown to be created
                    const $collection = $('.dt-button-collection');
                    if ($collection.find('.colvis-search').length === 0) {
                        // Create and inject search input
                        const $input = $('<input type="text" class="colvis-search" placeholder="Search columns...">');
                        $collection.prepend($input);

                        // Prevent click from closing the dropdown
                        $input.on('click', function (e) {
                            e.stopPropagation();
                        });

                        // Handle search filtering
                        $input.on('keyup', function (e) {
                            const term = $(this).val().toLowerCase();
                            $collection.find('.dt-button').each(function () {
                                const $btn = $(this);
                                const label = $btn.text().trim().toLowerCase();
                                if (term === '') {
                                    $btn.show();
                                    return;
                                }
                                $btn.toggle(label.includes(term));
                            });
                        });
                    }
            });
        }

        zoomBtn.addEventListener("click", () => {
            zoomOverlay.style.display = "flex";

            const zoomTable = zoomContent.querySelector('table');
            if (!window.DataTable) return;

            if (!zoomTable.dataset.initialized) {
                this.zoomTable = new DataTable(zoomTable, {
                    data: this.state.data,
                    ...this.state.dataTableSettings,
                    pageLength: 10,
                    lengthChange: true,
                    searchCols: this.state.columns.map(() => ({ search: '' })),
                    dom: 'Bfrtip',
                    columnControl: ['order', ['orderAsc', 'orderDesc', 'search']],
                    buttons: [
                        {
                            extend: 'colvis',
                            text: 'Show/Hide Columns',
                            className: 'btn btn-primary',
                            columns: ':gt(0)', // Hide first column by default
                            prefixButtons: [
                                {
                                    extend: 'colvisGroup',
                                    text: 'Hide All',
                                    show: ':hidden',
                                    hide: ':gt(0)'
                                },
                                {
                                    extend: 'colvisGroup',
                                    text: 'Show All',
                                    show: ':gt(0)',
                                }
                            ],
                            autoClose: false,
                            init: function (dt, node, config) {
                                showAllTextFilter(node);
                            }
                        }
                    ]
                });
                zoomTable.dataset.initialized = 'true';
            }
        });

        closeZoom.addEventListener("click", () => {
            zoomOverlay.style.display = "none";
            // Destroy DataTable in zoom view
            const zoomTable = zoomContent.querySelector('table');
            if (window.$ && window.$.fn.DataTable && window.$.fn.DataTable.isDataTable(zoomTable)) {
                window.$(zoomTable).DataTable().destroy();
                zoomTable.dataset.initialized = '';
            }
        });

        this.onKeyDown = (event) => {
            if (event.key === 'Escape' || event.key === 'Esc') {
                zoomOverlay.style.display = "none";
                const zoomTable = zoomContent.querySelector('table');
                if (window.$ && window.$.fn.DataTable && window.$.fn.DataTable.isDataTable(zoomTable)) {
                    window.$(zoomTable).DataTable().destroy();
                    zoomTable.dataset.initialized = '';
                }
            }
        };
        
        document.addEventListener('keydown', this.onKeyDown);

    }

    handleQuarterChange(direction) {
        const next = this.state.quarter?.[direction];
        if (!next) return;
        this.setState({ quarterNumber: next });
        this.fetchData();
    }

    setupLazyLoad() {
        const observer = new IntersectionObserver((entries, obs) => {
            for (const entry of entries) {
                if (entry.isIntersecting) {
                    this.loadTable();
                    obs.unobserve(this);
                }
            }
        }, {
            root: null,
            rootMargin: "100px",
            threshold: 0.1
        });

        observer.observe(this);
    }

    loadTable() {
        if (!this.state.isLoading) return;
        this.fetchData();
        this.render();
    }

    disconnectedCallback() {
                // Destroy main table
        if (this.table) {
            this.table.destroy();
            this.table = null;
        }

        // Destroy zoom table
        if (this.zoomTable) {
            this.zoomTable.destroy();
            this.zoomTable = null;
        }
        // Disconnect lazy‐load observer
        if (this.observer) {
            this.observer.disconnect();
            this.observer = null;
        }

        // Remove global Escape key handler
        if (this.onKeyDown) {
            document.removeEventListener('keydown', this.onKeyDown);
            this.onKeyDown = null;
        }
    }
}

customElements.define('data-table', DataTableComponent);
