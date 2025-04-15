(() => {
  // src/js/page_uploads.js
  FilePond.registerPlugin(FilePondPluginFileValidateType);
  FilePond.create(document.querySelector("#filepond"), {
    allowMultiple: true,
    storeAsFile: true,
    acceptedFileTypes: [
      "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
      "application/vnd.ms-excel"
    ],
    fileValidateTypeDetectType: (source, type) => new Promise((resolve) => {
      const name = source.name.toLowerCase();
      if (name.endsWith(".xls")) {
        return resolve("application/vnd.ms-excel");
      }
      if (name.endsWith(".xlsx")) {
        return resolve("application/vnd.openxmlformats-officedocument.spreadsheetml.sheet");
      }
      resolve(type);
    })
    // labelFileTypeNotAllowed: 'Apenas ficheiros Excel (.xls, .xlsx) são permitidos.',
    // fileValidateTypeLabelExpectedTypes: 'Tipos permitidos: {allTypes}'
  });
  function openEditModal(button) {
    const uuid = button.getAttribute("data-quarter-id");
    const number = button.getAttribute("data-quarter-number");
    const form = document.getElementById("edit-quarter-form");
    const input = document.getElementById("edit-quarter-number");
    input.value = number;
    form.action = `/quarters/edit/${uuid}/`;
  }
  document.addEventListener("click", (e) => {
    const target = e.target.closest(".upload-edit-link");
    if (target) {
      console.log("click");
      openEditModal(target);
    }
  });
})();
//# sourceMappingURL=page_uploads.js.map
