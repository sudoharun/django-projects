const buttons = document.getElementsByTagName('button')
const h1Headers = document.getElementsByTagName('h1')
const h2Headers = document.getElementsByTagName('h2')
const h3Headers = document.getElementsByTagName('h3')
const h4Headers = document.getElementsByTagName('h4')
const h5Headers = document.getElementsByTagName('h5')
const cards =  document.querySelectorAll('.cards > div')
const navBar = document.getElementById('navBar')
const navBarButtons = document.querySelectorAll('#navBar button')
const navBarMenuButton = document.getElementById('navBarMenuButton')
const navBarMenuButtonBasic = document.getElementById('navBarMenuButtonBasic')
const lineBreaks = document.getElementsByTagName('br')
const icons = document.getElementsByClassName('material-symbols-rounded')

Array.from(buttons).forEach(button => {
    button.classList.add('px-2', 'py-1', 'border', 'border-gray-400', 'bg-gray-200', 'text-black', 'rounded-md', 'shadow-md', 'w-full')
})

Array.from(h1Headers).forEach(h1 => {
    h1.classList.add('text-4xl', 'font-semibold', 'drop-shadow-xl')
})

Array.from(h2Headers).forEach(h2 => {
    h2.classList.add('text-3xl', 'font-semibold', 'drop-shadow-lg')
})

Array.from(h3Headers).forEach(h3 => {
    h3.classList.add('text-2xl', 'font-semibold', 'drop-shadow-md')
})

Array.from(h4Headers).forEach(h4 => {
    h4.classList.add('text-xl', 'font-semibold', 'drop-shadow-sm')
})

Array.from(h5Headers).forEach(h5 => {
    h5.classList.add('text-lg', 'font-semibold', 'drop-shadow-sm')
})

navBar.classList.add('p-2', 'border-b', 'border-gray-400', 'bg-gray-100', 'sticky', 'top-0')
Array.from(navBarButtons).forEach(button => {
    button.classList.remove('bg-gray-300')
    button.classList.add('bg-white', 'font-medium')
})

Array.from(lineBreaks).forEach(lineBreak => {
    lineBreak.remove()
})

Array.from(cards).forEach(card => {
    card.classList.add('border', 'border-gray-400', 'rounded-lg', 'p-2', 'shadow-lg', 'bg-gray-50')
})

navBarMenuButton.classList.remove('w-full')

navBarMenuButton.addEventListener('click', event => {
    let navBarElements = document.getElementsByClassName('navbar-element')
    Array.from(navBarElements).forEach(element => {
        element.classList.toggle('hidden')
    })
})

navBarMenuButtonBasic.addEventListener('click', event => {
    let navBarElements = document.getElementsByClassName('navbar-element-for-basic')
    Array.from(navBarElements).forEach(element => {
        element.classList.toggle('hidden')
    })
})

Array.from(icons).forEach(icon => {
    icon.classList.add('align-top')
})
