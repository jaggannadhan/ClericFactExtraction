const DOMAIN = "https://hopeful-flame-420906.uc.r.appspot.com/cleric";

async function getQuestionAndFacts() {
    const url = `${DOMAIN}/get_question_and_facts`;
    let answer = document.getElementById("answer");

    try {
        const response = await fetch(url, {
            method: "GET",
        });
  
        const result = await response.json();
        answer.innerHTML = JSON.stringify(result, undefined, 2);
        console.log("Success:", result);
        setAlertBanner(true, "Fetch Successful")
    } catch (error) {
        console.error("Error:", error);
        setAlertBanner(false, "Unable to complete request, Please try again later!")
    }
}

async function handleSubmit() {
    let question = document.getElementById("question").value;
    let documents = document.getElementById("documents").value;

    if(!question || !documents) {
        setAlertBanner(false, "Please fill in all the fields");
        return null;
    }

    let urls = getURLsFromString(documents);

    if(!urlCheck(urls)) {
        setAlertBanner(false, "Some/All of the URLs are incorrect!");
        return null;
    }

    const url = `${DOMAIN}/submit_question_and_documents`

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                question: question,
                documents: urls
            }),
        });
  
        const result = await response.json();
        console.log("Success:", result);
        setAlertBanner(true, "Question Submitted Successfully")
    } catch (error) {
        console.error("Error:", error);
        setAlertBanner(false, "Unable to complete request, Please try again later!")
    }
}

function getURLsFromString(urlString) {
    let urls = urlString.split(",").map(url => url.trim());
    return urls;
}

function urlCheck(urls) {
    const regex = /^(https?|ftp):\/\/(([a-z\d]([a-z\d-]*[a-z\d])?\.)+[a-z]{2,}|localhost)(\/[-a-z\d%_.~+]*)*(\?[;&a-z\d%_.~+=-]*)?(\#[-a-z\d_]*)?$/;
    let check = true;
    
    urls.forEach(url => {
        if(!regex.test(url.trim()))
            check = false;
    });
    
    return check;
}
 
function setAlertBanner(success, message) {
    let banner = document.getElementById("alert");
    banner.style.display = "block";
    banner.innerText = message;

    banner.style.background = success ? "#52df75" : "#dd4747";
    
    setTimeout(function() {
        banner.style.display = "none";
    }, 2000);
}
  

