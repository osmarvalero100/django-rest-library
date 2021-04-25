

if ($('#book_detail').length && $('#book_detail').data('id') > 0) {
    showBookDetail()
} else {
    buildLibrary()
}

async function buildLibrary() {
    let books = await fetchData('api/books/')

    for (const i in books) {
        let cover = (books[i].cover == '')? '/media/default.png' : books[i].cover
    
        $('#books').append(`<div class="col-md-4">
            <div class="card" style="width: 18rem;">
                <a href="/book/detail/${books[i].id}">
                    <img src="${cover}" class="card-img-top" alt="${books[i].name}">
                </a>
                <div class="card-body">
                    <hr>
                    <p><strong>${books[i].name}</strong></p>
                </div>
            </div>
        </div>`)
    }
}

async function showBookDetail() {
    let book_id = $('#book_detail').data('id')
    let book = await fetchData('api/books/'+book_id)
    console .log(book)
    let cover = (book.cover == '')? '/media/default.png' : book.cover
    let book_detail = `<div>
                            <h1>${book.name}</h1>
                            <p class="text-justify">${book.description}</p>
                            <hr>
                            <details>
                                <summary><strong>Autor:</strong> ${book.author.name}</summary>
                            </details>
                            <details>
                                <summary><strong>Editorial:</strong> ${book.editorial.name}</summary>
                            </details>
                            <details>
                                <summary><strong>N° páginas:</strong> ${book.number_pages}</summary>
                            </details>
                            <details>
                                <summary><strong>Idioma:</strong> ${book.language}</summary>
                            </details>
                        </div>`

    $('.img-book').html(`<img src="${cover}" alt="${book.name}">`)
    $('.book-desc').append(book_detail)
}