FilePond.registerPlugin(FilePondPluginFileValidateType);

FilePond.create(document.querySelector('#filepond'), {
    allowMultiple: true,
    storeAsFile: true,
    acceptedFileTypes: [
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.ms-excel'
    ],
    fileValidateTypeDetectType: (source, type) =>
        new Promise((resolve) => {
            const name = source.name.toLowerCase();

            if (name.endsWith('.xls')) {
                return resolve('application/vnd.ms-excel');
            }

            if (name.endsWith('.xlsx')) {
                return resolve('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet');
            }

            resolve(type);
        }),
    // labelFileTypeNotAllowed: 'Apenas ficheiros Excel (.xls, .xlsx) são permitidos.',
    // fileValidateTypeLabelExpectedTypes: 'Tipos permitidos: {allTypes}'
});

export function openEditModal(button) {
    const uuid = button.getAttribute('data-quarter-id');
    const number = button.getAttribute('data-quarter-number');
    const modalHeaderTitle = button.getAttribute('data-modal-title');

    const form = document.getElementById('edit-quarter-form');
    const numberInput = document.getElementById('edit-quarter-number');
    const precisionInput = document.getElementById('edit-quarter-precision');

    const modalHeader = document.getElementById('modal-title');

    modalHeader.textContent = modalHeaderTitle ?? 'Edit Files'

    numberInput.value = number;
    precisionInput.value = '9';  // Default value for new quarters

    if (uuid === 'new') {
        form.action = `/quarters/new/`;
    } else {
        form.action = `/quarters/edit/${uuid}/`;
        // If editing existing quarter, fetch its current precision
        fetch(`/api/quarters/${uuid}/`)
            .then(response => response.json())
            .then(data => {
                if (data.float_precision) {
                    precisionInput.value = data.float_precision;
                }
            })
            .catch(error => console.error('Error fetching quarter precision:', error));
    }
}

// Attach event listener to the document (delegation)
document.addEventListener("click", (e) => {
    const target = e.target.closest('.upload-edit-link');
    if (target) {
        openEditModal(target);
    }
});