(()=>{var y=Object.defineProperty;var m=Object.getOwnPropertySymbols;var f=Object.prototype.hasOwnProperty,w=Object.prototype.propertyIsEnumerable;var b=(n,t,e)=>t in n?y(n,t,{enumerable:!0,configurable:!0,writable:!0,value:e}):n[t]=e,h=(n,t)=>{for(var e in t||(t={}))f.call(t,e)&&b(n,e,t[e]);if(m)for(var e of m(t))w.call(t,e)&&b(n,e,t[e]);return n};var u=(n,t,e)=>new Promise((a,i)=>{var o=s=>{try{r(e.next(s))}catch(c){i(c)}},l=s=>{try{r(e.throw(s))}catch(c){i(c)}},r=s=>s.done?a(s.value):Promise.resolve(s.value).then(o,l);r((e=e.apply(n,t)).next())});var S=`${window.location.origin}/api/`,v=class extends HTMLElement{constructor(){super(),this.initState(),this.id=`table_${this.state.tableId}`,this.table=null}initState(){this.state={tableId:this.getAttribute("table_id")||"default",quarterNumber:this.getAttribute("q")||"1",data:[],columns:[{data:"name",title:"Name"},{data:"position",title:"Position"},{data:"office",title:"Office"},{data:"age",title:"Age"},{data:"startDate",title:"Start Date"},{data:"salary",title:"Salary"}],isError:!1,isLoading:!0,quarter:{current:"1",prev:null,next:"2"}}}static get observedAttributes(){return["table_id","q"]}connectedCallback(){this.setupLazyLoad()}fetchData(){return u(this,null,function*(){try{let t=[{name:"Tiger Nixon",position:"System Architect",office:"Edinburgh",age:61,startDate:"2011/04/25",salary:"$320,800"},{name:"Garrett Winters",position:"Accountant",office:"Tokyo",age:63,startDate:"2011/07/25",salary:"$170,750"},{name:"Ashton Cox",position:"Junior Technical Author",office:"San Francisco",age:66,startDate:"2009/01/12",salary:"$86,000"},{name:"Cedric Kelly",position:"Senior Javascript Developer",office:"Edinburgh",age:22,startDate:"2012/03/29",salary:"$433,060"},{name:"Airi Satou",position:"Accountant",office:"Tokyo",age:33,startDate:"2008/11/28",salary:"$162,700"}];this.setState({data:t,isLoading:!1})}catch(t){console.error("Error fetching table data:",t),this.setState({isError:!0})}finally{this.setState({isLoading:!1})}})}setState(t){this.state=h(h({},this.state),t),this.render()}renderSpinner(){return`<div class="spinner-container" role="status">
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
                    <h5 class="chart-title">Sample Data Table - Q${this.state.quarter.current}</h5>
                    <div class="chart-quarter-navigation"></div>
                </div>
                ${this.renderZoomOverlay()}
                <div class="chart-container" style="width:100%;height:400px;">
                    <div class="table-wrapper" style="width:100%;">
                        <table class="display responsive nowrap" style="width:100%">
                            <thead>
                                <tr>
                                    ${this.state.columns.map(e=>`
                                        <th>${e.title} <span class="filter-icon" data-column="${e.data}">\u{1F50D}</span></th>
                                    `).join("")}
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Data will be populated by DataTables -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>`;this.innerHTML!==t&&(this.innerHTML=t,this.initializeTable(),this.setupEvents(),this.renderQuarterNavigation())}renderQuarterNavigation(){let t=this.querySelector(`#${this.id} .chart-quarter-navigation`),{quarter:e}=this.state;t.innerHTML=`
            <button class="chart-quarter-nav-btn chart-zoom-btn"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 4H4m0 0v4m0-4 5 5m7-5h4m0 0v4m0-4-5 5M8 20H4m0 0v-4m0 4 5-5m7 5h4m0 0v-4m0 4-5-5"/></svg></button>
            <button ${e!=null&&e.prev?"":"disabled"} class="prev-quarter chart-quarter-nav-btn"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12l4-4m-4 4 4 4"/></svg></button>
            <button ${e!=null&&e.next?"":"disabled"} class="next-quarter chart-quarter-nav-btn"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 12H5m14 0-4 4m4-4-4-4"/></svg></button>`}renderZoomOverlay(){return`
            <div class="chart-zoom-overlay">
                <div class="chart-zoom-content">
                    <button class="chart-quarter-nav-btn chart-zoom-close"><svg class="w-6 h-6" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                        <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 9h4m0 0V5m0 4L4 4m15 5h-4m0 0V5m0 4 5-5M5 15h4m0 0v4m0-4-5 5m15-5h-4m0 0v4m0-4 5 5"/>
                    </svg></button>
                    <div class="chart-zoom-container" style="width:100%; height:100%;">
                        <table class="display responsive nowrap" style="width:100%">
                            <thead>
                                <tr>
                                    ${this.state.columns.map(t=>`
                                        <th>${t.title}</th>
                                    `).join("")}
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Data will be populated by DataTables -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        `}waitForDataTables(){return window.DataTable?Promise.resolve():new Promise(t=>{let e=()=>{window.DataTable?t():setTimeout(e,500)};e()})}initializeTable(){return u(this,null,function*(){if(this.table)return;yield this.waitForDataTables();let t=this.querySelector(`#${this.id} table`);t&&($.fn.DataTable.isDataTable(t)||(this.table=new DataTable(`#${this.id} table`,{data:this.state.data,columns:this.state.columns,responsive:!0,searching:!0,ordering:!0,paging:!0,language:{search:"Search table:"},destroy:!0})))})}createFilterPopover(t,e){let a=document.createElement("div");a.className="filter-popover";let i=document.createElement("input");i.type="text",i.placeholder=`Filter ${e}`;let o=document.createElement("div");o.className="filter-popover-buttons";let l=document.createElement("button");l.className="apply-btn",l.textContent="Apply";let r=document.createElement("button");r.className="clear-btn",r.textContent="Clear",o.appendChild(r),o.appendChild(l),a.appendChild(i),a.appendChild(o);let s=document.querySelector(`#${this.id} .filter-icon[data-column="${t}"]`),c=s.getBoundingClientRect();return a.style.top=`${c.bottom+5}px`,a.style.left=`${c.left}px`,l.addEventListener("click",()=>{let d=i.value;this.table.column(t).search(d).draw(),s.classList.toggle("active",d!==""),a.remove()}),r.addEventListener("click",()=>{i.value="",this.table.column(t).search("").draw(),s.classList.remove("active"),a.remove()}),document.addEventListener("click",d=>{!d.target.closest(".filter-popover")&&!d.target.closest(".filter-icon")&&a.remove()}),a}setupEvents(){var o,l;document.querySelectorAll(`#${this.id} .filter-icon`).forEach(r=>{r.addEventListener("click",s=>{s.stopPropagation();let c=r.dataset.column,d=r.parentElement.textContent.trim();document.querySelectorAll(".filter-popover").forEach(g=>g.remove());let p=this.createFilterPopover(c,d);document.body.appendChild(p),p.querySelector("input").focus()})}),(o=this.querySelector(`#${this.id} .prev-quarter`))==null||o.addEventListener("click",()=>this.handleQuarterChange("prev")),(l=this.querySelector(`#${this.id} .next-quarter`))==null||l.addEventListener("click",()=>this.handleQuarterChange("next"));let t=this.querySelector(`#${this.id} .chart-zoom-btn`),e=this.querySelector(`#${this.id} .chart-zoom-overlay`),a=this.querySelector(`#${this.id} .chart-zoom-container`),i=this.querySelector(`#${this.id} .chart-zoom-close`);t&&e&&a&&i&&(t.addEventListener("click",()=>{e.style.display="flex",new DataTable(a.querySelector("table"),{data:this.state.data,columns:this.state.columns,responsive:!0,searching:!0,ordering:!0,paging:!0,language:{search:"Search table:"}})}),i.addEventListener("click",()=>{e.style.display="none";let r=a.querySelector("table");$.fn.DataTable.isDataTable(r)&&$(r).DataTable().destroy()}),document.addEventListener("keydown",r=>{if(r.key==="Escape"||r.key==="Esc"){e.style.display="none";let s=a.querySelector("table");$.fn.DataTable.isDataTable(s)&&$(s).DataTable().destroy()}}))}handleQuarterChange(t){var a;let e=(a=this.state.quarter)==null?void 0:a[t];e&&(this.setState({quarterNumber:e}),this.fetchData())}setupLazyLoad(){new IntersectionObserver((e,a)=>{for(let i of e)i.isIntersecting&&(this.loadTable(),a.unobserve(this))},{root:null,rootMargin:"100px",threshold:.1}).observe(this)}loadTable(){this.state.isLoading&&(this.fetchData(),this.render())}disconnectedCallback(){this.table&&(this.table.destroy(),this.table=null)}};customElements.define("data-table",v);})();
//# sourceMappingURL=table_webcomponent.js.map
