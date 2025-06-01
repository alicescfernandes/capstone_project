(()=>{var C=Object.defineProperty,S=Object.defineProperties;var k=Object.getOwnPropertyDescriptors;var u=Object.getOwnPropertySymbols;var f=Object.prototype.hasOwnProperty,w=Object.prototype.propertyIsEnumerable;var g=(s,e,t)=>e in s?C(s,e,{enumerable:!0,configurable:!0,writable:!0,value:t}):s[e]=t,d=(s,e)=>{for(var t in e||(e={}))f.call(e,t)&&g(s,t,e[t]);if(u)for(var t of u(e))w.call(e,t)&&g(s,t,e[t]);return s},p=(s,e)=>S(s,k(e));var y=(s,e)=>{var t={};for(var a in s)f.call(s,a)&&e.indexOf(a)<0&&(t[a]=s[a]);if(s!=null&&u)for(var a of u(s))e.indexOf(a)<0&&w.call(s,a)&&(t[a]=s[a]);return t};var v=(s,e,t)=>new Promise((a,l)=>{var r=o=>{try{i(t.next(o))}catch(c){l(c)}},n=o=>{try{i(t.throw(o))}catch(c){l(c)}},i=o=>o.done?a(o.value):Promise.resolve(o.value).then(r,n);i((t=t.apply(s,e)).next())});var T=`${window.location.origin}/api/`,x=document.createElement("style");x.textContent=`
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
`;document.head.appendChild(x);window.$.fn.dataTable&&(window.$.fn.dataTable.ext.errMode="none");var m=class extends HTMLElement{constructor(){super(),this.initState(),this.id=`table_${this.state.chartSlug}`,this.table=null}initState(){this.state={chartSlug:this.getAttribute("chart_slug"),quarterNumber:this.getAttribute("q"),data:[],columns:[],isError:!1,isLoading:!0,quarter:{current:"1",prev:null,next:null},dataTableSettings:{responsive:!0,searching:!0,ordering:!0,paging:!0,destroy:!0,debug:!1,pageLength:5,lengthChange:!1,language:{search:"Search table:"}}}}static get observedAttributes(){return["chart_slug","q"]}connectedCallback(){this.setupLazyLoad()}fetchData(){return v(this,null,function*(){let e=new URLSearchParams(d({slug:this.state.chartSlug,q:this.state.quarterNumber},this.state.selectedOption&&{opt:this.state.selectedOption}));try{let a=yield fetch(`${T}chart/?${e.toString()}`);if(!a.ok)throw new Error(`HTTP error! Status: ${a.status}`);let l=yield a.json();console.log("data",l);let t=l,{selected_option:r}=t,n=y(t,["selected_option"]);this.setState(d({selectedOption:r||""},n))}catch(a){this.setState({isError:!0})}finally{this.setState({isLoading:!1})}})}fetchData2(){return v(this,null,function*(){try{let e=[{name:"Tiger Nixon",position:"System Architect",office:"Edinburgh",age:61,startDate:"2011/04/25",salary:"$320,800"},{name:"Garrett Winters",position:"Accountant",office:"Tokyo",age:63,startDate:"2011/07/25",salary:"$170,750"},{name:"Ashton Cox",position:"Junior Technical Author",office:"San Francisco",age:66,startDate:"2009/01/12",salary:"$86,000"},{name:"Cedric Kelly",position:"Senior Javascript Developer",office:"Edinburgh",age:22,startDate:"2012/03/29",salary:"$433,060"},{name:"Airi Satou",position:"Accountant",office:"Tokyo",age:33,startDate:"2008/11/28",salary:"$162,700"}],t=[{data:"name",title:"Name"},{data:"position",title:"Position"},{data:"office",title:"Office"},{data:"age",title:"Age"},{data:"startDate",title:"Start Date"},{data:"salary",title:"Salary"}];this.setState({data:e,columns:t})}catch(e){console.error("Error fetching table data:",e),this.setState({isError:!0})}finally{this.setState({isLoading:!1})}})}setState(e){this.state=d(d({},this.state),e),this.render()}renderSpinner(){return`<div class="spinner-container" role="status">
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
        `}render(){if(this.state.isLoading){this.innerHTML=this.renderSpinner();return}if(this.state.isError){this.innerHTML=this.renderError();return}let e=`
            <div id="${this.id}">
                <div class="chart-header">
                    <h5 class="chart-title">Sample Data Table - Q${this.state.quarter.current}</h5>
                    <div class="chart-quarter-navigation"></div>
                </div>
                ${this.renderZoomOverlay()}
                <div class="chart-container" style="width:100%;height:400px;">
                    <table class="display responsive nowrap" style="width:100%"></table>
                </div>
            </div>`;this.innerHTML!==e&&(this.innerHTML=e,this.initializeTable(),this.setupEvents(),this.renderQuarterNavigation())}renderQuarterNavigation(){let e=this.querySelector(`#${this.id} .chart-quarter-navigation`),{quarter:t}=this.state;e.innerHTML=`
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
        `}waitForDataTables(){return window.DataTable?Promise.resolve():new Promise(e=>{let t=()=>{window.DataTable?e():setTimeout(t,500)};t()})}initializeTable(){return v(this,null,function*(){if(this.table)return;yield this.waitForDataTables();let e=this.querySelector(`#${this.id} table`);e&&($.fn.DataTable.isDataTable(e)||(this.table=new DataTable(`#${this.id} table`,p(d({data:this.state.data,columns:this.state.columns.map((t,a)=>p(d({},t),{render:(l,r,n,i)=>r==="display"?`<div class="d-flex justify-content-between align-items-center">
                            <span>${l}</span>
                        </div>`:l,title:`<div class="dt-column-header">
                    <span class="dt-column-title">${t.title}</span>
                    <span class="filter-icon" data-column="${a}">
                        <svg width="16" height="16" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M15 1H1L6.09 8.59V13L9.91 14V8.59L15 1Z" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                        </svg>
                    </span>
                </div>`}))},this.state.dataTableSettings),{initComplete:()=>{this.setupFilterEvents()}}))))})}setupFilterEvents(){document.querySelectorAll(`#${this.id} .filter-icon`).forEach(t=>{t.replaceWith(t.cloneNode(!0))}),document.querySelectorAll(`#${this.id} .filter-icon`).forEach(t=>{t.addEventListener("click",a=>{console.log("click",a.x,a.y),a.stopPropagation();let l=parseInt(t.dataset.column),r=t.closest(".dt-column-header").querySelector(".dt-column-title").textContent.trim();document.querySelectorAll(".filter-popover").forEach(i=>i.remove());let n=this.createFilterPopover(l,r,a.x,a.y);this.appendChild(n),n.querySelector("input").focus()})})}createFilterPopover(e,t,a,l){let r=document.createElement("div");r.className="filter-popover";let n=document.createElement("input");n.type="text",n.placeholder=`Filter ${t}`;let i=document.createElement("div");i.className="filter-popover-buttons";let o=document.createElement("button");o.className="apply-btn",o.textContent="Apply";let c=document.createElement("button");return c.className="clear-btn",c.textContent="Clear",i.appendChild(c),i.appendChild(o),r.appendChild(n),r.appendChild(i),r.style.position="absolute",r.style.top=`${l+20}px`,r.style.left=`${a-100}px`,r.style.zIndex="10",this.appendChild(r),o.addEventListener("click",h=>{let b=n.value;this.table.column(e).search(b).draw(),document.querySelector(`#${this.id} .filter-icon[data-column="${e}"]`).classList.toggle("active",b!==""),r.remove()}),c.addEventListener("click",()=>{n.value="",this.table.column(e).search("").draw(),document.querySelector(`#${this.id} .filter-icon[data-column="${e}"]`).classList.remove("active"),r.remove()}),n.addEventListener("keypress",h=>{h.key==="Enter"&&o.click()}),document.addEventListener("click",h=>{!h.target.closest(".filter-popover")&&!h.target.closest(".filter-icon")&&r.remove()}),r}setupEvents(){var r,n;(r=this.querySelector(`#${this.id} .prev-quarter`))==null||r.addEventListener("click",()=>this.handleQuarterChange("prev")),(n=this.querySelector(`#${this.id} .next-quarter`))==null||n.addEventListener("click",()=>this.handleQuarterChange("next"));let e=this.querySelector(`#${this.id} .chart-zoom-btn`),t=this.querySelector(`#${this.id} .chart-zoom-overlay`),a=this.querySelector(`#${this.id} .chart-zoom-container`),l=this.querySelector(`#${this.id} .chart-zoom-close`);e.addEventListener("click",()=>{t.style.display="flex";let i=a.querySelector("table");window.DataTable&&(i.dataset.initialized||(new DataTable(i,p(d({data:this.state.data,columns:this.state.columns},this.state.dataTableSettings),{pageLength:10,lengthChange:!0})),i.dataset.initialized="true"))}),l.addEventListener("click",()=>{t.style.display="none";let i=a.querySelector("table");window.$&&window.$.fn.DataTable&&window.$.fn.DataTable.isDataTable(i)&&(window.$(i).DataTable().destroy(),i.dataset.initialized="")}),document.addEventListener("keydown",i=>{if(i.key==="Escape"||i.key==="Esc"){t.style.display="none";let o=a.querySelector("table");window.$&&window.$.fn.DataTable&&window.$.fn.DataTable.isDataTable(o)&&(window.$(o).DataTable().destroy(),o.dataset.initialized="")}})}handleQuarterChange(e){var a;let t=(a=this.state.quarter)==null?void 0:a[e];t&&(this.setState({quarterNumber:t}),this.fetchData())}setupLazyLoad(){new IntersectionObserver((t,a)=>{for(let l of t)l.isIntersecting&&(this.loadTable(),a.unobserve(this))},{root:null,rootMargin:"100px",threshold:.1}).observe(this)}loadTable(){this.state.isLoading&&(this.fetchData(),this.render())}disconnectedCallback(){this.table&&(this.table.destroy(),this.table=null)}};customElements.define("data-table",m);})();
//# sourceMappingURL=table_webcomponent.js.map
