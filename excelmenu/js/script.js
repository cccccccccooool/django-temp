// 预定义选项
window.onload = () => {
    fetch('/1')  // 替换成你的实际API路径
        .then(response => response.json())
        .then(data => {
            allOp = data;
            initializeSelects();
            nextMuen(document.querySelectorAll('.categorySelect')[0]);
        })
        .catch(error => console.error('Error:', error));
};

document.addEventListener('DOMContentLoaded', (event) => {
        const dateInput = document.getElementById('date');
        dateInput.value = new Date().toISOString().split('T')[0];
});

let allOp = {};

function initializeSelects() {
    const categorySelects = document.querySelectorAll('.categorySelect');
    categorySelects.forEach(select => {
        // 清空现有选项
        select.innerHTML = '';
        // 添加新选项
        for (let category in allOp) {
            let option = document.createElement('option');
            option.value = category;
            option.textContent = category;
            select.appendChild(option);
        }
        select.onchange = function() { nextMuen(this); };
    });

    const secondMenus = document.querySelectorAll('.secondMenu');
    secondMenus.forEach(select => {
        select.onchange = function() { updateInput(this); };
    });
}

function nextMuen(categorySelect) {
    var row = categorySelect.closest('tr');
    var secondMenuSelect = row.querySelector('.secondMenu');
    var customInput = row.querySelector('.customInput');
    secondMenuSelect.innerHTML = "";

    var selectValue = categorySelect.value;
    var xqElement = allOp[selectValue];

    // 添加一个默认选项
    var defaultOption = document.createElement("option");
    defaultOption.text = "请选择";
    defaultOption.value = "";
    secondMenuSelect.add(defaultOption);

    for (var i = 0; i < xqElement.length; i++) {
        var option = document.createElement("option");
        option.text = xqElement[i];
        secondMenuSelect.add(option);
    }
    secondMenuSelect.style.display = "inline-block";
    customInput.style.display = "inline-block";
}

function updateInput(selectElement) {
    var row = selectElement.closest('tr');
    var customInput = row.querySelector('.customInput');
    customInput.value = selectElement.value;
}

function addRow() {
    const table = document.querySelector('tbody');
    const newRow = table.rows[0].cloneNode(true);
    newRow.querySelectorAll('input').forEach(input => input.value = '');

    var categorySelect = newRow.querySelector('.categorySelect');
    var secondMenu = newRow.querySelector('.secondMenu');
    var customInput = newRow.querySelector('.customInput');
    var uniqueId = 'row-' + (table.rows.length + 1);
    categorySelect.id = 'categorySelect-' + uniqueId;
    secondMenu.id = 'secondMenu-' + uniqueId;
    customInput.id = 'customInput-' + uniqueId;

    // 重置二级菜单和自定义输入
    secondMenu.innerHTML = '';
    secondMenu.style.display = 'none';
    customInput.value = '';

    table.appendChild(newRow);
    updateRowNumbers();
}

function downloadPDF() {
    // 隐藏所有的select元素
    const selects1 = document.getElementsByClassName('secondMenu');
    const selects2 = document.getElementsByClassName('categorySelect');
    Array.from(selects1).forEach(select => select.style.display = 'none');
    Array.from(selects2).forEach(select => select.style.display = 'none');


    const element = document.getElementById('dataForm');
    console.log('Starting PDF generation...');

    html2pdf().from(element).save()
    .then(() => {
        console.log('PDF generated and download triggered.');
        // 恢复所有select元素的显示
        Array.from(selects1).forEach(select => select.style.display = '');
        Array.from(selects2).forEach(select => select.style.display = '');
    })
    .catch(error => {
        console.error('Error during PDF generation:', error);
        // 确保即使出错也恢复显示
        selects.forEach(select => select.style.display = '');
    });
}

function updateRowNumbers() {
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach((row, index) => {
        row.querySelector('td:first-child').textContent = index + 1;
    });
}