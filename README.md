# Project-1-Vet-Management-App

<section class="section about">
<h2 class="h2">About</h2>
<p class="p">This was an individual project completed during week 5 of the CodeClan course.  We were given a choice of 4 briefs on the Thursday and would present our app to our colleagues the following Thursday. </p>
</section>

<section class="section screenshots">
<h2 class="h2">Screenshots</h2>
<p class="p">For a short video preview of the app, please visit my  <a href="https://g-dunlop.github.io/g-dunlop-portfolio-website/">portfolio site</a>:
<table class="table">
  <tr class="tr">
    <td class="td"><img class="img" width="1158" alt="vma_1_homepage" src="https://user-images.githubusercontent.com/88304522/166954895-d69c28dd-0dd3-47e4-8468-1fe36346cd59.png"></td>
    <td class="td"><img class="img" width="1280" alt="vma_2_vets_page" src="https://user-images.githubusercontent.com/88304522/166954890-d5936b12-a3f4-488e-9366-e4c5123284ce.png"></td>
    <td class="td"><img class="img" width="1160" alt="vma_3_vet_homepage" src="https://user-images.githubusercontent.com/88304522/166954873-8e256c1a-a83b-4c81-a82d-bf4b78325e01.png"></td>
  </tr>
  <tr class="tr">
    <td class="td"><img class="img" width="1268" alt="vma4_animal_homepage" src="https://user-images.githubusercontent.com/88304522/166954989-c9e050dc-3040-4da3-83ba-51d3afaf3ba3.png"></td>
    <td class="td"><img class="img" width="1268" alt="vma5_admin_dropdown" src="https://user-images.githubusercontent.com/88304522/166954971-7d2b8c5f-0ae2-4eca-a974-001378fdd622.png"></td>
    <td class="td"><img class="img" width="1268" alt="vma6_all_animals" src="https://user-images.githubusercontent.com/88304522/166954968-73f55def-65d6-4a1c-80b9-88358242e919.png"></td>
  </tr>
  <tr class="tr">
    <td class="td"><img class="img" width="1268" alt="vma7_animals_search" src="https://user-images.githubusercontent.com/88304522/166954964-9fef866d-587c-48b8-a8a3-59a482e3881a.png"></td>
    <td class="td"><img class="img" width="1268" alt="vma8_animals_searchresult" src="https://user-images.githubusercontent.com/88304522/166954960-cb9d782d-f2f3-42ff-aea6-5a9a68b62581.png"></td>
    <td class="td"><img class="img" width="1268" alt="vma9_newappointmentform" src="https://user-images.githubusercontent.com/88304522/166954947-92d611b1-1695-4e5e-b04d-668b728b0073.png"></td>
  </tr>
 </table>

<section class="section tools">
<h2 class="h2">Tools</h2>
<ul class="ul">
  <li class="li">Python</li>
  <li class="li">Flask</li>
  <li class="li">Jinja</li>
  <li class="li">PostgreSQL</li>
 </ul>
</section>

<section class="section brief">
<h2 class="h2">Project Brief</h2>
<p class="p">A veterinary practice has approached you to build a web application to help them manage their animals and vets. A vet may look after many animals at a time. An animal is registered with only one vet.</p>

<section class="section mvp">
<h4 class="h4">MVP</h4>
  <ul class="ul">
    <li class="li">The practice wants to be able to register / track animals. Important information for the vets to know is:
      <ul class="ul">
        <li class="li">Name</li>
        <li class="li">Date Of Birth (use a VARCHAR initially)</li>
        <li class="li">Type of animal</li>
        <li class="li">Contact details for the owner</li>
        <li class="li">Treatment notes</li>
      </ul>
    </li>
    <li class="li">Be able to assign animals to vets</li>
    <li class="li">CRUD actions for vets / animals</li>
   </ul>
   </section>
   
   <section class="section extensions">
 <h4 class="h4">Possible Extensions</h4>
  <ul class="ul">
  <li class="li">Mark owners as unregistered.  Unregistered owners can't add animals </li>
  <li class="li">Owners can have multiple animals</li>
  <li class="li">Add search bar to index.html pages to find animals/owners quickly</li>
  <li class="li">Sort animals/owners alphabetically</li>
  <li class="li">Add CRUD functionality for appointments and treatments</li>
  <li class="li">Vets/animals display upcoming appointments arranged by date.  Also, display past appointments for animals so we can see their treatment history.</li>
  </ul>
  </section>
  
  <section class="section planning">
  <h4 class="h4">Planning</h4>
  <p class="p">The below images demonstrate some of my planning for the MVP stage of the project.  I made use of: Class and Object Diagrams, Wireframes, a Db Table Diagram, a MSCW board and a useCase Diagram.
 
  <table class="table">
    <tr class="tr">
    <td class="td">
        <img class="img" width="1268" src="https://user-images.githubusercontent.com/88304522/166924212-9f2ffb33-398d-4f0d-a9e9-c92789f32c44.png"/>
      </td>
     <td class="td">
        <img class="img" width="1268" src="https://user-images.githubusercontent.com/88304522/166924388-c00aca84-ee71-4a09-a83c-11405077a461.png"/>
      </td>
    <td class="td">
        <img class="img" width="1268" src="https://user-images.githubusercontent.com/88304522/166924505-23eead73-4c99-43c2-bdde-c9351745d265.jpg"/>
      </td>
    </tr>
    <tr class="tr">
      <td class="td">
        <img class="img" width="1268" src="https://user-images.githubusercontent.com/88304522/166925430-d838c32c-5c22-427d-bf95-9c75480f9e6b.png"/>
      </td>
     <td class="td">
        <img class="img" width="1268" src="https://user-images.githubusercontent.com/88304522/166925523-0f93b573-a75b-48ea-9d15-e5f53529a480.png"/>
      </td>
      <td class="td">
        <img class="img" width="1268" src="https://user-images.githubusercontent.com/88304522/166925610-0fdd5457-b976-48b0-8c8d-ca0bae61a86c.png"/>
      </td>
    </tr>
   </table>





<h2 class="h2">How to Run</h2>
<ul class="ul">
  <li class="li">clone repository to local computer</li>
  <li class="li">pip install flask</li>
  <li class="li">python3 console.py</li>
  <li class="li">flask run</li>
 </ul>

<h2 class="h2">What I learned</h2>

<ul class="ul">
  <li class="li">I learned a lot about RESTful routes in this project and using repositories and controllers to link back-end data to the front-end.</li>
  <li class="li">I became more comfortable with passing variables around, especially into Jinja templates.</li>
  <li class="li">I learner that I need to really think through what I'm trying to do in terms of extensions and the user journey.  I don't feel I had a clear user in mind, ense the app not really looking like a professional piece of software.  For extensions, I need to plan with the same care and consideration that I give at the start to the MVP.</li>
</ul>

<h2 class="h2">What I would do differently</h2>
<ul class="ul">
  <li class="li">I would like to make it impossible to double book vet appointments if there is a time conflict, although I feel this will be more possible in JavaScript.</li>
  <li class="li">I feel like there are some navigation issues and we need less clicks for users to get where they want to go, perhap more information together on one page rather than separate pages for everything.</li>
  <li class="li">Users need confirmation/feedback for form completion/updates (They need to know what they've done worked!), plus appropriate redirects after form submission.</li>
</ul>


