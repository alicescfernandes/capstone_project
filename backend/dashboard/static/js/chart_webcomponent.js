(() => {
  var __defProp = Object.defineProperty;
  var __getOwnPropSymbols = Object.getOwnPropertySymbols;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __propIsEnum = Object.prototype.propertyIsEnumerable;
  var __defNormalProp = (obj, key, value) => key in obj ? __defProp(obj, key, { enumerable: true, configurable: true, writable: true, value }) : obj[key] = value;
  var __spreadValues = (a, b) => {
    for (var prop in b || (b = {}))
      if (__hasOwnProp.call(b, prop))
        __defNormalProp(a, prop, b[prop]);
    if (__getOwnPropSymbols)
      for (var prop of __getOwnPropSymbols(b)) {
        if (__propIsEnum.call(b, prop))
          __defNormalProp(a, prop, b[prop]);
      }
    return a;
  };
  var __objRest = (source, exclude) => {
    var target = {};
    for (var prop in source)
      if (__hasOwnProp.call(source, prop) && exclude.indexOf(prop) < 0)
        target[prop] = source[prop];
    if (source != null && __getOwnPropSymbols)
      for (var prop of __getOwnPropSymbols(source)) {
        if (exclude.indexOf(prop) < 0 && __propIsEnum.call(source, prop))
          target[prop] = source[prop];
      }
    return target;
  };
  var __async = (__this, __arguments, generator) => {
    return new Promise((resolve, reject) => {
      var fulfilled = (value) => {
        try {
          step(generator.next(value));
        } catch (e) {
          reject(e);
        }
      };
      var rejected = (value) => {
        try {
          step(generator.throw(value));
        } catch (e) {
          reject(e);
        }
      };
      var step = (x) => x.done ? resolve(x.value) : Promise.resolve(x.value).then(fulfilled, rejected);
      step((generator = generator.apply(__this, __arguments)).next());
    });
  };

  // src/js/chart_webcomponent.js
  var API_BASE_URL = `${window.location}api/`;
  var PlotlyChart = class extends HTMLElement {
    constructor() {
      super();
      this.initState();
      this.id = `chart_${this.state.chartSlug}`;
    }
    initState() {
      this.state = {
        chartSlug: this.getAttribute("chart_slug"),
        quarterNumber: this.getAttribute("q"),
        isError: false,
        isLoading: true
      };
    }
    static get observedAttributes() {
      return ["chart_slug"];
    }
    connectedCallback() {
      this.setupLazyLoad();
    }
    fetchData() {
      return __async(this, null, function* () {
        const params = new URLSearchParams(__spreadValues({
          slug: this.state.chartSlug,
          q: this.state.quarterNumber
        }, this.state.selectedOption && { opt: this.state.selectedOption }));
        try {
          const res = yield fetch(`${API_BASE_URL}chart/?${params.toString()}`);
          if (!res.ok) throw new Error(`HTTP error! Status: ${res.status}`);
          const data = yield res.json();
          const _a = data, { selected_option } = _a, rest = __objRest(_a, ["selected_option"]);
          this.setState(__spreadValues({
            selectedOption: selected_option || ""
          }, rest));
        } catch (e) {
          this.setState({ isError: true });
        } finally {
          this.setState({ isLoading: false });
        }
      });
    }
    setState(newState) {
      this.state = __spreadValues(__spreadValues({}, this.state), newState);
      this.render();
    }
    render() {
      if (this.state.isLoading) return this.renderSpinner();
      if (this.state.isError) return this.renderError();
      const hasOptions = Array.isArray(this.state.options) && this.state.options.length > 0;
      this.innerHTML = `
            <div id="${this.id}">
                <div class="chart-header">
                    <h5 class="chart-title"></h5>
                    <div class="chart-quarter-navigation"></div>
                </div>
                ${hasOptions ? `<p>Filter By: <select class="chart-filter"></select></p>` : ""}
                <div class="chart" style="width:100%;height:400px;"></div>
            </div>`;
      this.renderChart();
      this.renderQuarterNavigation();
      if (hasOptions) {
        this.renderOptions();
        this.setupEvents();
      }
    }
    renderQuarterNavigation() {
      const container = this.querySelector(`#${this.id} .chart-quarter-navigation`);
      const { quarter } = this.state;
      console.log("quarter", quarter, !(quarter == null ? void 0 : quarter.prev));
      container.innerHTML = `
            <button ${!(quarter == null ? void 0 : quarter.prev) ? "disabled" : ""} class="prev-quarter chart-quarter-nav-btn">\u2190</button>
            <button ${!(quarter == null ? void 0 : quarter.next) ? "disabled" : ""} class="next-quarter chart-quarter-nav-btn">\u2192</button>`;
    }
    renderSpinner() {
      this.innerHTML = `<div class="spinner-container" role="status">
                                <svg aria-hidden="true" class="spinner-svg" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                                    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
                                </svg>
                                <span class="sr-only">Loading...</span>`;
    }
    renderError() {
      this.innerHTML = `
            <div class="alert-error" role="alert">
            <svg class="alert-error-svg" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
            </svg>
            <span class="sr-only">Info</span>
            <div>
                <span class="font-bold">Unable to render chart.</span> Try uploading a new one with the data.
            </div>
            </div>
        `;
    }
    renderEmptyState() {
      return `
            <div class="alert-info" role="alert">
                <svg class="shrink-0 inline w-4 h-4 me-3" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
                </svg>
                <span class="sr-only">Info</span>
                <div>
                    The graph doesn't have data to show.
                </div>
            </div>
        `;
    }
    renderOptions() {
      const select = this.querySelector(`#${this.id} .chart-filter`);
      if (!select) return;
      const { options, selectedOption } = this.state;
      select.innerHTML = options.map((opt) => `<option value="${opt}" ${opt === selectedOption ? "selected" : ""}>${opt}</option>`).join("");
    }
    setupEvents() {
      var _a, _b, _c;
      (_a = this.querySelector(`#${this.id} .chart-filter`)) == null ? void 0 : _a.addEventListener("change", (e) => {
        this.setState({ selectedOption: e.target.value });
        this.fetchData();
      });
      (_b = this.querySelector(`#${this.id} .prev-quarter`)) == null ? void 0 : _b.addEventListener("click", () => this.handleQuarterChange("prev"));
      (_c = this.querySelector(`#${this.id} .next-quarter`)) == null ? void 0 : _c.addEventListener("click", () => this.handleQuarterChange("next"));
    }
    handleQuarterChange(direction) {
      var _a;
      const next = (_a = this.state.quarter) == null ? void 0 : _a[direction];
      if (!next) return;
      this.setState({ quarterNumber: next });
      this.fetchData();
    }
    renderChart() {
      return __async(this, null, function* () {
        if (!this.isConnected || this.state.isLoading) return;
        const { title, chart_config, quarter } = this.state;
        const { traces, layout } = chart_config;
        const container = this.querySelector(`#${this.id} .chart`);
        this.querySelector(`#${this.id} .chart-title`).textContent = `${title} - Q${quarter.current}`;
        if (!traces.length) {
          container.innerHTML = this.renderEmptyState();
          return;
        }
        Plotly.newPlot(container, traces, layout, { responsive: true });
      });
    }
    setupLazyLoad() {
      const observer = new IntersectionObserver((entries, obs) => {
        for (const entry of entries) {
          if (entry.isIntersecting) {
            this.loadChart();
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
    loadChart() {
      if (!this.state.isLoading) return;
      this.fetchData();
      this.render();
    }
  };
  window.addEventListener("load", () => {
    customElements.define("plotly-chart", PlotlyChart);
  });
})();
//# sourceMappingURL=chart_webcomponent.js.map
