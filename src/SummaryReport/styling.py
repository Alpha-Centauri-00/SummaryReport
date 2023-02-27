
css = """


.content-table {
    border-collapse: collapse;
    margin: 70px 0;
    font-size: 0.9em;
    min-width: 400px;
    border-radius: 5px 5px 0 0;
    box-shadow: 0 0 20px rgba(0 0 0 / 25%);
}

th {
    background-color: #009879;
    color: #ffffff;
    text-align: left;
    font-weight: bold;
    resize: horizontal;
    overflow: auto;
    height: 25px;
    position: sticky;
    top: 0;
    z-index: 1;
    background-color: #009879;
    color: white;
}

.content-table th,
.content-table td{
    padding: 12px 15px;
}
.content-table tbody tr{
    border-bottom: 1px solid #dddddd;
}



.edit{
    
    -webkit-user-modify:read-write-plaintext-only;
    color: black;
    font-family: 'Courier New', Courier, monospace;
    
}



tr:hover {
    background-color: rgb(228, 226, 226);
    transform: scale(1);
    box-shadow: 2px 2px 12px rgba(0, 0, 0, 0.2), -1px -1px 8px rgba(0, 0, 0, 0.2);
}


h1 {
    font-weight: 600;
    text-align: center;
    background-color: #009879;
    color: white;
    padding: 10px 0px;
    border-radius: 5px;
    font-family: 'Courier New', Courier, monospace;
}

.label.Pass{
    background-color: #97bd61;
    color: #fff;
    font-weight: bold;
}
.label.Fail{
    background-color: #ce3e01;
    color: #fff;
    font-weight: bold;
    font-size:13px;
}
.label.Skip{
    background-color: #fed84f;
    color: #fff;
    font-weight: bold;  
    font-size:13px;
}

.label {
    text-align: center;
    padding: 2px 5px;
    font-size: 0.75em;
    letter-spacing: 1px;
    /* white-space: nowrap; */
    border-radius: 3px;
    padding: 10;
}
.SummNum{
    /* text-align: right; */
    font-size: 5ch;
    
    margin: 1%;
    padding: 1px;
    width: max-content;
    border: 1px solid blue;
    float: left;
    /* font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif; */
    
}

.pie {
    --p:100;
    --b:22px;
    /* --c:#97bd61; */
    --w:150px;
    
    width:var(--w);
    aspect-ratio:1;
    position:relative;
    display:inline-grid;
    margin:5px;
    place-content:center;
    font-size:25px;
    font-weight:bold;
    font-family:sans-serif;
    /* color: #37a98c; */
    color: black;
}

.pie:before,
.pie:after {
    content:"";
    position:absolute;
    border-radius:50%;
}
.pie:before {
    inset:0;
    background:
    radial-gradient(farthest-side,var(--c) 98%,#0000) top/var(--b) var(--b) no-repeat,
    conic-gradient(var(--c) calc(var(--p)*1%),#0000 0);
    -webkit-mask:radial-gradient(farthest-side,#0000 calc(99% - var(--b)),#000 calc(100% - var(--b)));
        mask:radial-gradient(farthest-side,#0000 calc(99% - var(--b)),#000 calc(100% - var(--b)));
}
.pie:after {
    inset:calc(50% - var(--b)/2);
    background:var(--c);
    transform:rotate(calc(var(--p)*3.6deg)) translateY(calc(50% - var(--w)/2));
}
.animate {
    animation:p 1s .5s both;
}
.piepass{
    --c:#97bd61;
}
.piefail{
    --c:#ce3e01;
}
.pieskip{
    --c:#fed84f;
}
.section{
    float: left;
    padding: 1%;
}

.section { margin-bottom: 1em; color: black; cursor: pointer; font-family: 'Courier New', Courier, monospace; font-size: small; font-weight: bold;}

.printer{
    /* position: absolute; */
    padding-right: 1em;
    float: right;
    color: black;
    font-weight: bold;
    font-family: 'Courier New', Courier, monospace;
}

@media print {
    #printPageButton {
      display: none;
    }
  }



"""
