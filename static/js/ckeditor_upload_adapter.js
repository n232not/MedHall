class UploadAdapter {
    constructor(loader) {
        this.loader = loader;
    }

    upload() {
        return this.loader.file.then(
            file =>
                new Promise((resolve, reject) => {
                    const data = new FormData();
                    data.append("upload", file);

                    fetch("/ckeditor/upload/", {
                        method: "POST",
                        body: data,
                    })
                        .then(response => response.json())
                        .then(result => resolve({ default: result.url }))
                        .catch(error => reject(error));
                })
        );
    }
}

function SimpleUploadAdapterPlugin(editor) {
    editor.plugins.get("FileRepository").createUploadAdapter = loader => {
        return new UploadAdapter(loader);
    };
}

ClassicEditor.create(document.querySelector("#editor"), {
    extraPlugins: [SimpleUploadAdapterPlugin]
});
