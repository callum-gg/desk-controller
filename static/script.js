function ChangeInput(inp) {
    console.log(JSON.stringify({ inp }))
    try {
        fetch('/changeInput', {
            method: 'POST',
            body: JSON.stringify({ inp }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
    } catch (error) {
        alert("an error occured: " + error)
    }
}