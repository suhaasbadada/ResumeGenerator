function addNewWEField(){
    //console.log("Adding new field")
    
    let newNode=document.createElement('textarea')
    newNode.classList.add('form-control');
    newNode.classList.add('weField');
    newNode.classList.add("mt-2");
    newNode.setAttribute("rows",3);
    newNode.setAttribute("placeholder","Enter Details");
    
    let weOb=document.getElementById('we');
    let weAddButtonOb=document.getElementById("weAddButton");
    
    
    weOb.insertBefore(newNode,weAddButtonOb);
    
    }
    
    
    function addNewAQField(){
        
        let newNode=document.createElement('textarea')
        newNode.classList.add('form-control');
        newNode.classList.add('eqField');
        newNode.classList.add("mt-2");
        newNode.setAttribute("rows",3);
        newNode.setAttribute("placeholder","Enter Details");
        
        let aqOb=document.getElementById('aq');
        let aqAddButtonOb=document.getElementById("aqAddButton");
        
        
        aqOb.insertBefore(newNode,aqAddButtonOb);
        
    }
    
    function addNewprojField(){
        
        let newNode=document.createElement('textarea')
        newNode.classList.add('form-control');
        newNode.classList.add('projField');
        newNode.classList.add("mt-2");
        newNode.setAttribute("rows",3);
        newNode.setAttribute("placeholder","Enter Details");
        
        let aqOb=document.getElementById('pj');
        let projAddButtonOb=document.getElementById("projAddButton");
        
        
        aqOb.insertBefore(newNode,projAddButtonOb);
        
    }

    function addNewtechField(){
        
        let newNode=document.createElement('textarea')
        newNode.classList.add('form-control');
        newNode.classList.add('techField');
        newNode.classList.add("mt-2");
        newNode.setAttribute("rows",3);
        newNode.setAttribute("placeholder","Enter Details");
        
        let projOb=document.getElementById('ts');
        let techAddButtonOb=document.getElementById("techAddButton");
        
        
        projOb.insertBefore(newNode,techAddButtonOb);
        
    }

    function addNewsoftField(){
        
        let newNode=document.createElement('textarea')
        newNode.classList.add('form-control');
        newNode.classList.add('techField');
        newNode.classList.add("mt-2");
        newNode.setAttribute("rows",3);
        newNode.setAttribute("placeholder","Enter Details");
        
        let tsOb=document.getElementById('ss');
        let softAddButtonOb=document.getElementById("softAddButton");
        
        
        tsOb.insertBefore(newNode,softAddButtonOb);
        
    }





    
    
    function generateCV(){
        let nameField=document.getElementById('nameField').value;
    
        document.getElementById('nameT1').innerHTML=nameField;
        document.getElementById('nameT2').innerHTML=nameField; 
    
        let contactField=document.getElementById('contactField').value;
        document.getElementById('contactT').innerHTML=contactField;

        let contactField=document.getElementById('emailField').value;
        document.getElementById('emailT').innerHTML=contactField;        
    
        let addrField=document.getElementById('addrField').value;
        document.getElementById('addressT').innerHTML=addrField;
        
    
        let gitField=document.getElementById('gitField').value;
        document.getElementById('gitT').innerHTML=gitField;

        
        let linkedField=document.getElementById('linkedField').value;
        document.getElementById('linkedT').innerHTML=linkedField;
        
        let wes=document.getElementsByClassName('weField');
        let str1=''
        for(let e of wes){
            str1=str1+`<li> ${e.value}</li>`;
        }
        document.getElementById('weT').innerHTML=str1;
    
    
        let aqs=document.getElementsByClassName('eqField');
        let str2=''
        for(let e of aqs){
            str2=str2+`<li> ${e.value}</li>`;
        }
        document.getElementById('aqT').innerHTML=str2;


        let prjs=document.getElementsByClassName('projField');
        let str3=''
        for(let e of prjs){
            str3=str3+`<li> ${e.value}</li>`;
        }
        document.getElementById('pjT').innerHTML=str3;

        let tss=document.getElementsByClassName('techField');
        let str4=''
        for(let e of tss){
            str4=str4+`<li> ${e.value}</li>`;
        }
        document.getElementById('tsT').innerHTML=str4;

        let sss=document.getElementsByClassName('softField');
        let str5=''
        for(let e of sss){
            str5=str5+`<li> ${e.value}</li>`;
        }
        document.getElementById('ssT').innerHTML=str5;
    
        document.getElementById('cvf').style.display='none';
        document.getElementById('cv-template').style.display='block';
         
    }   
    
    
    