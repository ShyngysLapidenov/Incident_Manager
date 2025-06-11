$(document).ready(function () {
    $('#create-form').on('submit', function (e) {
        e.preventDefault();
        const title = $('input[name="title"]').val();
        const description = $('textarea[name="description"]').val();
        $.ajax({
            url: '/create',
            method: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({ title, description }),
            success: () => location.reload()
        });
    });

    $('.resolve-btn').on('click', function () {
        const li = $(this).closest('li');
        const id = li.data('id');
        $.ajax({
            url: '/resolve/' + id,
            method: 'POST',
            success: function () {
                li.find('.resolve-btn').remove();
                li.html(li.html().replace('new', 'resolved'));
            }
        });
    });
});
