from pesummary.core.webpage.webpage import make_html, open_html

make_html(
    web_dir="../", pages=["home"], stylesheets=[], title="Charlie Hoy"
)
index = open_html("../", "../", "home")
index.add_content(
"""
    <script src='./js/navigation.js'></script>
    <link rel="stylesheet" href="./css/fa-code.css">
    <link rel="stylesheet" href="./css/parallax.css">
    <link rel="stylesheet" href="./css/text.css">

<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
<style>
@media only screen and (max-width:749px) {
  .parallax1 {
    background-attachment: inherit;
  }
  .parallax2 {
    background-attachment: inherit;
  }
}
</style>
<div class="parallax1"></div>
<h1 id="name">Charlie<br>Hoy<br></h1>
<h1 id="occupation">PhD student</h1>
<div class="container" style="position: absolute; left: 11%; top:410px">
<a href='https://www.google.co.uk' class="fa fa-facebook-square" style="font-size: 30px; padding-right: 3px"></a>
<a href='http://linkedin.com/in/charlie-hoy-46405a161' class="fa fa-linkedin-square" style="font-size: 30px; padding-right: 3px"></a>
<a href='https://github.com/hoyc1' class="fa fa-github-square" style="font-size: 30px; padding-right: 3px"></a>
<a href='https://git.ligo.org/charlie.hoy' class="fa fa-gitlab" style="font-size: 30px; padding-right: 3px"></a>
<a href="mailto:hoyc1@cardiff.ac.uk" class="fa fa-envelope" style="font-size: 30px; padding-right: 3px"></a>
</div>

<div class="container" style="position: absolute; left: 50%; margin-left: -150px; top:475px; border-style: solid; border-width: thick; border-color: #f8f8ff; height: 450px; width: 300px">
    <img src="./images/charliehoy.jpg" style="width: 250px; position: absolute; margin-top: 10px" href="https://scholar.google.com/citations?view_op=list_works&hl=en&authuser=1&user=wjjomcQAAAAJ&gmla=AJsN-F6xnalxEPJ-nK_7H_R0RRFxJA9kpJ6af7mKkULPtRTS0ch-kAu4xF_GgLdeu_Dg95EQwJOk3mUC1qS2aVas2waVCwiIe-D1i6cwM8QZjKXServlZzA"></img>
    <div class="row justify-content-center">
    <a href='https://scholar.google.com/citations?view_op=list_works&hl=en&authuser=1&user=wjjomcQAAAAJ&gmla=AJsN-F6xnalxEPJ-nK_7H_R0RRFxJA9kpJ6af7mKkULPtRTS0ch-kAu4xF_GgLdeu_Dg95EQwJOk3mUC1qS2aVas2waVCwiIe-D1i6cwM8QZjKXServlZzA' data-toggle='tooltip'>
    <h1 style="margin-top: 350px; font-size: 24px; color: #f8f8ff">Google Scholar page</h1>
    </a>
    </div>
</div>

<div class="parallax2"></div>

<div class="container">
<div class="row justify-content-center" style="position: absolute; left: 50%; margin-left: -45%; top:1000px; width: 90%">
<div class="container" style="border-style: solid; border-width: thick; border-color: #f8f8ff; padding-bottom: 2%;">
<div class="card job" style="margin-top: 20px;">
    <div class="card-header bg-dark text-white">
        PhD student, <span class="institution">Cardiff University</span> (2018-Present)
    </div>
    <div class="card-body">
      <i>Proposed thesis title: Binary Black Hole Astrophysics</i>,

<ul class="pt-2">
<li>Understanding when precession can be measured from a compact binary coalesence</li>
<li>Inferring the preferred spin distribution of Black Holes</li>
</ul>

Funded by STFC
    </div>
  </div>
</div>
<div class="container" style="border-style: solid; border-width: thick; border-color: #f8f8ff; padding-bottom: 2%">
<div class="card job" style="margin-top: 20px">
    <div class="card-header bg-dark text-white">
        Other interests
    </div>
    <div class="card-body">
<ul class="pt-2">
<li>Software development</li>
<li>Numerically solving Einstein's equations</li>
<li>Modelling binary black populations</li>
</ul>
    </div>
  </div>
</div>
</div>
</div>

<div class="container" style="padding-bottom: 5%">
<h1 id="publication">Papers</h1>
<h1 style="margin-top: 10px" id="publicationtext">The list below includes all publications on which I had a significant contribution to the work presented. Not included are a number of publications on which I am named as an author by virtue of being a member of the LIGO Scientific Collaboration.</h1>
<div style="margin-top: 50px">
<script src="https://bibbase.org/show?bib=https%3A%2F%2Fraw.githubusercontent.com%2Fhoyc1%2Fhoyc1.github.io%2Fmaster%2Fsrc%2Fbibtex.bib&jsonp=1"></script>
</div>
</div>
<div class="bg-dark text-light" style="background-color: lightgrey; padding-bottom: 5%">
<div class="container">
<h1 id="awards">Awards</h1>
<table class="table" style="width:100%; background-color: #f8f8ff; border-color: #f8f8ff margin-bottom: 100px">
  <tr>
    <td><a href="https://cqgplus.com/2019/05/13/charlie-hoy-and-lasse-schmieding-win-best-student-talk-prizes-at-britgrav-2019/">Best student talk prizes at Britgrav 2019, Durham</a></td>
  </tr>
  <tr>
    <td>Best poster at the Early Career Researcher poster competition 2019, Cardiff</td>
  </tr>
  <tr>
    <td>$1500 AUSD grant to support travel to Melbourne, Australia for the Parameter Estimation workshop, 2019</td>
  </tr>
</table>
  </div>
</div>
</div>
</div>

<div class="container" style="padding-bottom: 5%">
<h1 id="media">In the media</h1>

<div class="bibbase_group_whole" id="news_2020">
  <div class="bibbase_group" onclick="toggleGroup('news_2020')" onkeypress="toggleGroup('news_2020')" tabindex="0">
    <i class="fa bibbase_group_head_icon fa-angle-down"></i>&nbsp;
    <span>2020</span>
    <span class="bibbase_group_count">
      (2)
    </span>
  </div>
  <div class="bibbase_group_body" style="display: block;">
    <div class="bibbase_paper" id="bbc-'Blackneutronstar'discoverychangesastronomy-2020">
      <span class="bibbase_paper_titleauthoryear">
        <span class="bibbase_paper_title">
          <a href="https://www.bbc.co.uk/news/science-environment-53151106">
            'Black neutron star' discovery changes astronomy
          </a>
        </span>
        <span class="bibbase_paper_author">
          BBC News
        </span>
      </span>
      <i>23rd June 2020</i>
      <span class="note"></span>
      <span class="bibbase_note"></span>
      <br class="bibbase_paper_content">
        <span class="bibbase_paper_content dontprint">
          <a href="#" onclick="showBib(event); return false;" class="bibbase bibtex link">See more
            <i class="fa fa-caret-down"></i>
          </a>
        </span>
      </br>
      <div class="well well-small bibbase" data-type="bibtex" style="display:none">
        <pre style="white-space: pre-wrap;">
        Scientists have discovered an astronomical object that has never been observed before. It is more massive than collapsed stars, known as "neutron stars", but has less mass than black holes. Such "black neutron stars" were not thought possible and will mean ideas for how neutron stars and black holes form will need to be rethought. The discovery was made by an international team using gravitational wave detectors in the US and Italy. Charlie Hoy, a PhD student from Cardiff University, UK, involved in the study...
        </pre>
      </div>
    </div>

    <div class="bibbase_paper" id="cardiff-cardiffstudentatthecentreofligosmysteriournewdiscovery-2020">
      <span class="bibbase_paper_titleauthoryear">
        <span class="bibbase_paper_title">
          <a href="https://www.cardiff.ac.uk/news/view/2408694-cardiff-student-at-the-centre-of-ligos-mysterious-new-discovery">
            Cardiff Student at centre of LIGOs mysterious new discovery
          </a>
        </span>
        <span class="bibbase_paper_author">
          Cardiff University
        </span>
      </span>
      <i>23rd June 2020</i>
      <span class="note"></span>
        <span class="bibbase_note"></span>
        <br class="bibbase_paper_content">
          <span class="bibbase_paper_content dontprint">
            <a href="#" onclick="showBib(event); return false;" class="bibbase bibtex link">See more
              <i class="fa fa-caret-down"></i>
            </a>
          </span>

        <div class="well well-small bibbase" data-type="bibtex" style="display:none">
          <pre style="white-space: pre-wrap;">
        A Cardiff University student has found himself at the centre of a major breakthrough discovery that could potentially help to solve a decades-old mystery. Charlie Hoy, currently in the third year of his PhD and a member of the Laser Interferometer Gravitational Wave Observatory (LIGO) Scientific Collaboration...
          </pre>
        </div>
      </div>

    <div class="bibbase_paper" id="ligo-pressrelease-2020">
      <span class="bibbase_paper_titleauthoryear">
        <span class="bibbase_paper_title">
          <a href="https://www.ligo.org/detections/GW190814/pr-english.pdf">
            LIGO-Virgo Finds Mystery Object in 'Mass Gap'
          </a>
        </span>
        <span class="bibbase_paper_author">
          LIGO Scientific Collaboration
        </span>
      </span>
      <i>23rd June 2020</i>
      <span class="note"></span>
        <span class="bibbase_note"></span>
        <br class="bibbase_paper_content">
          <span class="bibbase_paper_content dontprint">
            <a href="#" onclick="showBib(event); return false;" class="bibbase bibtex link">See more
              <i class="fa fa-caret-down"></i>
            </a>
          </span>

        <div class="well well-small bibbase" data-type="bibtex" style="display:none">
          <pre style="white-space: pre-wrap;">
            When the most massive stars die, they collapse under their own gravity and leave behind black holes; when stars that are a bit less massive die, they explode in supernovas and leave behind dense, dead remnants of stars called neutron stars.
          </pre>
        </div>
      </div>
    </div>
  </div>

<div class="bibbase_group_whole" id="news_2019">
  <div class="bibbase_group" onclick="toggleGroup('news_2019')" onkeypress="toggleGroup('news_2019')" tabindex="0">
    <i class="fa bibbase_group_head_icon fa-angle-down"></i>&nbsp;
    <span>2019</span>
    <span class="bibbase_group_count">
      (1)
    </span>
  </div>
  <div class="bibbase_group_body" style="display: block;">
    <div class="bibbase_paper" id="cqgplus-charliehoywinbeststudenttalkprizeatbritgrav-2019">
      <span class="bibbase_paper_titleauthoryear">
        <span class="bibbase_paper_title">
          <a href="https://cqgplus.com/2019/05/13/charlie-hoy-and-lasse-schmieding-win-best-student-talk-prizes-at-britgrav-2019/">
            Charlie Hoy and Lasse Schmieding win best student talk prizes at Britgrav 2019
          </a>
        </span>
        <span class="bibbase_paper_author">
          CGQ+
        </span>
      </span>
      <i>13th May 2019</i>
      <span class="note"></span>
      <span class="bibbase_note"></span>
      <br class="bibbase_paper_content">
        <span class="bibbase_paper_content dontprint">
          <a href="#" onclick="showBib(event); return false;" class="bibbase bibtex link">See more
            <i class="fa fa-caret-down"></i>
          </a>
        </span>
      </br>
      <div class="well well-small bibbase" data-type="bibtex" style="display:none">
        <pre style="white-space: pre-wrap;">
	We are delighted to award Charlie Hoy and Lasse Schmieding the CQG-sponsored best student talk prize, for their talks at the recent Britgrav 2019 conference, held at Durham University...
        </pre>
      </div>
    </div>
  </div>
</div>
</div>

<style>
/* Responsive columns */
@media screen and (max-width: 600px) {
  .column {
    width: 100%;
    display: block;
    margin-bottom: 20px;
  }
}
</style>

<div class="bg-warning text-light" style="background-color: yellow; margin-top: 10px; padding-bottom: 5%">
<div class="container">
<h1 id="git_projects">Git projects</h1>
<div class="card-columns">
   <div class="column">
      <div class="card mb-4 bg-dark text-light">
        <div class="card-body">
          <h3 class="card-title">PESummary</h3>
          <p class="card-text">A collaboration-driven Python package providing tools for generating summary pages for all sample generating codes.<br><img src="https://badge.fury.io/py/pesummary.svg"></img><img src="https://img.shields.io/conda/vn/conda-forge/pesummary.svg" style="margin-left: 5px"></img><br><img src="https://img.shields.io/pypi/dm/pesummary"></img><img src="https://anaconda.org/conda-forge/pesummary/badges/downloads.svg" style="margin-left: 5px"></img>
        </p></div>
        <div class="card-footer">
          <a href="https://git.ligo.org/lscsoft/pesummary" target="_blank"><i class="fa fa-gitlab" style="padding-right: 5px;"></i>lscsoft/pesummary</a><br>
          <a href="https://github.com/pesummary/pesummary" target="_blank"><i class="fa fa-github" style="padding-right: 5px;"></i>pesummary/pesummary</a>
        </div>
      </div>
      <div class="card mb-4 bg-dark text-light">
        <div class="card-body">
          <h3 class="card-title">This website</h3>
          <p class="card-text">Source code for this website written in HTML, CSS and Javascript
        </p></div>
        <div class="card-footer">
          <a href="https://github.com/hoyc1/hoyc1.github.io" target="_blank"><i class="fa fa-github" style="padding-right: 5px;"></i>hoyc1/hoyc1.github.io</a>
        </div>
      </div>
   </div>
</div>
</div>
</div>
<div class="bg-dark text-light" style="margin-bottom: 10px; height: 70px">
  <div class="row justify-content-center" style="margin-top: 10px; margin-left: 0px; margin-right: 0px">
    <h1 style="font-size: 30px">© Charlie Hoy</h1>
  </div>
    <h1 style="font-size: 30px">© Charlie Hoy</h1>
  </div>
</div>
"""
)
