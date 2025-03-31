class AdminSetup {

  /**
   * Setup global data
   */
  constructor() {
    // Get current page
    this.currentPage = document.querySelector('.content h1').textContent.toLowerCase().trim()
    console.log(this.currentPage)

    // Run methods in each page
    this.autorun()
  }

  /**
   * Setup Tagify for the given input selector
   * @param {string} inputSelector - The selector for the input element
   */
  #setupTagify(inputSelector) {
    const input = document.querySelector(inputSelector)
    if (input) {
      const tagify = new Tagify(input, {
        whitelist: [],
        dropdown: {
          classname: "color-blue",
          enabled: 0,
          maxItems: 5
        }
      })
    }
  }

  /**
   * Setup the style for the top menu links
   */
  #setupTopmenuLinksStyle() {
    const menuItems = document.querySelectorAll('.d-sm-inline-block a.nav-link')
    menuItems.forEach(item => {
      item.classList.add('btn')
      item.classList.add('btn-primary')
      item.classList.add('text-light')
    })
  }

  #setupMarkDown() {

    // Get text areas
    const noMarkdownIds = [""]
    let textAreasSelector = 'div > textarea'
    textAreasSelector = noMarkdownIds.map(id => `${textAreasSelector}:not(#id_${id})`).join(", ")
    const textAreas = document.querySelectorAll(textAreasSelector)

    setTimeout(() => {
      textAreas.forEach(textArea => {

        new SimpleMDE({
          element: textArea,
          toolbar: [
            "bold", "italic", "heading", "|",
            "quote", "code", "link", "image", "|",
            "unordered-list", "ordered-list", "|",
            "undo", "redo", "|",
            "preview",
          ],
          spellChecker: false,
        })
      })
    }, 100)
  }

  /**
   * Run the functions for the current page
   */
  autorun() {

    setTimeout(() => {
      // Global methods
      this.#setupTopmenuLinksStyle()

      // Methods to run for each page
      const methods = {
        "documentos": [() => {this.#setupTagify('[name="palabras_clave"]')}],
        "respuestas": [this.#setupMarkDown],
      }

      // Run the methods for the current page
      if (methods[this.currentPage]) {
        for (let method of methods[this.currentPage]) {
          method.call(this)
        }
      }

    }, 100)

  }
}

new AdminSetup()