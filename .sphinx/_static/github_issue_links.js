window.onload = function() {
    const link = document.createElement("a");
    link.classList.add("muted-link");
    link.classList.add("github-issue-link");
    link.text = "Give feedback";
    link.href = "mailto:snap-store-docs-feedback@lists.canonical.com";
    link.target = "_blank";

    const div = document.createElement("div");
    div.classList.add("github-issue-link-container");
    div.append(link)

    const container = document.querySelector(".article-container > .content-icon-container");
    container.prepend(div);
};
