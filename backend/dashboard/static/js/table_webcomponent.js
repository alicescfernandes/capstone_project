(()=>{var L=Object.defineProperty,z=Object.defineProperties;var q=Object.getOwnPropertyDescriptors;var h=Object.getOwnPropertySymbols;var x=Object.prototype.hasOwnProperty,y=Object.prototype.propertyIsEnumerable;var f=(r,t,e)=>t in r?L(r,t,{enumerable:!0,configurable:!0,writable:!0,value:e}):r[t]=e,d=(r,t)=>{for(var e in t||(t={}))x.call(t,e)&&f(r,e,t[e]);if(h)for(var e of h(t))y.call(t,e)&&f(r,e,t[e]);return r},C=(r,t)=>z(r,q(t));var T=(r,t)=>{var e={};for(var a in r)x.call(r,a)&&t.indexOf(a)<0&&(e[a]=r[a]);if(r!=null&&h)for(var a of h(r))t.indexOf(a)<0&&y.call(r,a)&&(e[a]=r[a]);return e};var v=(r,t,e)=>new Promise((a,o)=>{var n=s=>{try{i(e.next(s))}catch(c){o(c)}},l=s=>{try{i(e.throw(s))}catch(c){o(c)}},i=s=>s.done?a(s.value):Promise.resolve(s.value).then(n,l);i((e=e.apply(r,t)).next())});var D=`${window.location.origin}/api/`,k=document.createElement("style");k.textContent=`
    .dt-column-header {
        position: relative;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .filter-icon {
        cursor: pointer;
        opacity: 0.5;
        transition: opacity 0.2s;
        display: inline-flex;
        align-items: center;
        margin-left: 4px;
    }
    .filter-icon:hover {
        opacity: 1;
    }
    .filter-icon.active {
        opacity: 1;
        color: #2563eb;
    }
    .filter-popover {
        position: absolute;
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 12px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1);
        z-index: 1000;
        min-width: 200px;
    }
    .filter-popover input {
        width: 100%;
        padding: 8px;
        border: 1px solid #e5e7eb;
        border-radius: 4px;
        margin-bottom: 8px;
    }
    .filter-popover-buttons {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
    }
    .filter-popover button {
        padding: 6px 12px;
        border-radius: 4px;
        border: 1px solid #e5e7eb;
        background: white;
        cursor: pointer;
        transition: all 0.2s;
    }
    .filter-popover button:hover {
        background: #f3f4f6;
    }
    .filter-popover .apply-btn {
        background: #2563eb;
        color: white;
        border-color: #2563eb;
    }
    .filter-popover .apply-btn:hover {
        background: #1d4ed8;
    }
    .dt-button-collection {
        max-height: 300px !important;
        overflow-y: auto !important;
    }
    .buttons-colvis-search {
        margin-bottom: 10px !important;
        width: 100% !important;
        padding: 8px !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 4px !important;
    }
    .dt-button-collection .dt-button {
        width: 100% !important;
        text-align: left !important;
        margin: 2px 0 !important;
    }
`;document.head.appendChild(k);window.$.fn.dataTable&&(window.$.fn.dataTable.ext.errMode="none");var w=class extends HTMLElement{constructor(){super(),this.initState(),this.id=`table_${this.state.chartSlug}`,this.table=null,this.zoomTable=null}initState(){this.state={chartSlug:this.getAttribute("chart_slug"),quarterNumber:this.getAttribute("q"),data:[],columns:[],isError:!1,isLoading:!0,quarter:{current:"1",prev:null,next:null},dataTableSettings:{responsive:!0,searching:!0,ordering:!0,paging:!0,destroy:!0,debug:!1,pageLength:5,lengthChange:!1,search:{smart:!1,caseInsensitive:!0},searchCols:[],language:{search:"Search table:"}}}}static get observedAttributes(){return["chart_slug","q"]}connectedCallback(){this.setupLazyLoad()}fetchData(){return v(this,null,function*(){let t=new URLSearchParams({slug:this.state.chartSlug,q:this.state.quarterNumber});try{let a=yield fetch(`${D}chart/?${t.toString()}`);if(!a.ok)throw new Error(`HTTP error! Status: ${a.status}`);let o=yield a.json();console.log("data",o);let e=o,{selected_option:n}=e,l=T(e,["selected_option"]);this.setState(d({selectedOption:n||""},l))}catch(a){this.setState({isError:!0})}finally{this.setState({isLoading:!1})}})}setState(t){this.state=d(d({},this.state),t),this.render()}renderSpinner(){return`<div class="spinner-container" role="status">
            <svg aria-hidden="true" class="spinner-svg" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
            </svg>
            <span class="sr-only">Loading...</span>
        </div>`}renderError(){return`
            <div class="alert-error" role="alert">
                <svg class="alert-error-svg" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 .5a9.5 9.5 0 1 0 9.5 9.5A9.51 9.51 0 0 0 10 .5ZM9.5 4a1.5 1.5 0 1 1 0 3 1.5 1.5 0 0 1 0-3ZM12 15H8a1 1 0 0 1 0-2h1v-3H8a1 1 0 0 1 0-2h2a1 1 0 0 1 1 1v4h1a1 1 0 0 1 0 2Z"/>
                </svg>
                <span class="sr-only">Info</span>
                <div>
                    <span class="font-bold">Unable to load table data.</span> Please try again later.
                </div>
            </div>
        `}render(){if(this.state.isLoading){this.innerHTML=this.renderSpinner();return}if(this.state.isError){this.innerHTML=this.renderError();return}let t=`
            <div id="${this.id}">
                <div class="chart-header">
                    <h5 class="chart-title">${this.state.title} - Q${this.state.quarter.current}</h5>
                    <div class="chart-quarter-navigation">${this.renderQuarterNavigation()}</div>
                </div>
                ${this.renderZoomOverlay()}
                <div class="chart-container" style="width:100%;height:400px;">
                    <table class="display responsive nowrap" style="width:100%"></table>
                </div>
            </div>`;this.innerHTML=t,this.initializeTable(),this.setupEvents(),this.renderQuarterNavigation()}renderQuarterNavigation(){let{quarter:t}=this.state;return`
            <button class="chart-quarter-nav-btn chart-zoom-btn"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H4m0 0v4m0-4 5 5m7-5h4m0 0v4m0-4-5 5M8 20H4m0 0v-4m0 4 5-5m7 5h4m0 0v-4m0 4-5-5"/></svg></button>
            <button ${t!=null&&t.prev?"":"disabled"} class="prev-quarter chart-quarter-nav-btn"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12l4-4m-4 4 4 4"/></svg></button>
            <button ${t!=null&&t.next?"":"disabled"} class="next-quarter chart-quarter-nav-btn"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 12H5m14 0-4 4m4-4-4-4"/></svg></button>`}renderZoomOverlay(){return`
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
        `}waitForDataTables(){return window.DataTable?Promise.resolve():new Promise(t=>{let e=()=>{window.DataTable?t():setTimeout(e,500)};e()})}initializeTable(){return v(this,null,function*(){if(this.table)return;yield this.waitForDataTables();let t=this.querySelector(`#${this.id} table`);t&&($.fn.DataTable.isDataTable(t)||(this.table=new DataTable(`#${this.id} table`,d({data:this.state.data,columns:this.state.columns},this.state.dataTableSettings))))})}setupEvents(){var n,l;(n=this.querySelector(`#${this.id} .prev-quarter`))==null||n.addEventListener("click",()=>this.handleQuarterChange("prev")),(l=this.querySelector(`#${this.id} .next-quarter`))==null||l.addEventListener("click",()=>this.handleQuarterChange("next"));let t=this.querySelector(`#${this.id} .chart-zoom-btn`),e=this.querySelector(`#${this.id} .chart-zoom-overlay`),a=this.querySelector(`#${this.id} .chart-zoom-container`),o=this.querySelector(`#${this.id} .chart-zoom-close`);t.addEventListener("click",()=>{e.style.display="flex";let i=a.querySelector("table");window.DataTable&&(i.dataset.initialized||(this.zoomTable=new DataTable(i,C(d({data:this.state.data},this.state.dataTableSettings),{pageLength:10,lengthChange:!0,searchCols:this.state.columns.map(()=>({search:""})),dom:"Bfrtip",columnControl:["order",["orderAsc","orderDesc","search"]],buttons:[{extend:"colvis",text:"Show/Hide Columns",className:"btn btn-primary",columns:":gt(0)",prefixButtons:[{extend:"colvisGroup",text:"Hide All",show:":hidden",hide:":gt(0)"},{extend:"colvisGroup",text:"Show All",show:":gt(0)"}],autoClose:!1,init:function(s){$(s).on("click",function(c){let u=$(".dt-button-collection");if(u.find(".colvis-search").length===0){let p=$('<input type="text" class="colvis-search" placeholder="Search columns...">');u.prepend(p),p.on("click",function(g){g.stopPropagation()}),p.on("keyup",function(g){console.log($(this).val().toLowerCase());let m=$(this).val().toLowerCase();u.find(".dt-button").each(function(){let b=$(this),S=b.text().trim().toLowerCase();if(m===""){b.show();return}b.toggle(S.includes(m))})})}})}}]})),i.dataset.initialized="true"))}),o.addEventListener("click",()=>{e.style.display="none";let i=a.querySelector("table");window.$&&window.$.fn.DataTable&&window.$.fn.DataTable.isDataTable(i)&&(window.$(i).DataTable().destroy(),i.dataset.initialized="")}),document.addEventListener("keydown",i=>{if(i.key==="Escape"||i.key==="Esc"){e.style.display="none";let s=a.querySelector("table");window.$&&window.$.fn.DataTable&&window.$.fn.DataTable.isDataTable(s)&&(window.$(s).DataTable().destroy(),s.dataset.initialized="")}})}handleQuarterChange(t){var a;let e=(a=this.state.quarter)==null?void 0:a[t];e&&(this.setState({quarterNumber:e}),this.fetchData())}setupLazyLoad(){new IntersectionObserver((e,a)=>{for(let o of e)o.isIntersecting&&(this.loadTable(),a.unobserve(this))},{root:null,rootMargin:"100px",threshold:.1}).observe(this)}loadTable(){this.state.isLoading&&(this.fetchData(),this.render())}disconnectedCallback(){this.table&&(this.table.destroy(),this.table=null)}};customElements.define("data-table",w);})();
//# sourceMappingURL=table_webcomponent.js.map
