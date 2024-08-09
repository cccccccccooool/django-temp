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

function updateRowNumbers() {
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach((row, index) => {
        row.querySelector('td:first-child').textContent = index + 1;
    });
}