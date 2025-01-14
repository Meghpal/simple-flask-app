let update_feedback = (rid, feedback) => {
    fetch("/update", {
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        method: "POST",
        body: JSON.stringify({ rid: rid, feedback: feedback })
    })
        .then(resp => window.location.href = "/feedback.html/submit")
        .catch(err => console.log(err.message));
}