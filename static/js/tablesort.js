/* function sortTableByColumn(table, column, asc = true) {
    const dirModifier = asc ? 1 : -1;
    const tBody = table.tBodies[0];
    const rows = Array.from(tBody.querySelectorAll("tr"));

    // Sort each row
    const sortedRows = rows.sort((a, b) => {
        const aColText = a.querySelector('td:nth-child(${ column + 1 })').textContent.trim();
        const bColText = b.querySelector('td:nth-child(${ column + 1 })').textContent.trim();

        return aColText > bColText ? (1 * dirModifier) : (-1 * dirModifier);
    });

    console.log(sortedRows);
}

sortTableByColumn(document.querySelector("table"), 1); */

function sortTable(n) {
    var table = document.querySelector('table'),
        thead = document.querySelector('thead'),
        tbody = table.querySelector('tbody')
        bRows = [...tbody];

    bRows.sort( (a, b) => {
        console.log(a,b);
    })

}