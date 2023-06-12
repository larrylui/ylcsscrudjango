var cTemplate = Template7.compile(`
    <p>This is a sample for dynamic text: 
    <span class="keyword">{{title}}</span>
    </p>
`)

function showSample(title) {
    document.getElementById("app").innerHTML = cTemplate({title: title})
}
