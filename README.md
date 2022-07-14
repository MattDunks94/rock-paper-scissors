# Rock, Paper, Scissors Application

<p>Rock, Paper, Scissors application is a Python terminal game, based on the classic hand game, which runs in the Code Institute mock terminal on Heroku.</p>
<p>Users face the challenge of beating the computer by choosing between rock, paper or scissors.</p>
<a href="https://rock-paper-scissors-python-app.herokuapp.com/">Live version of project.<a>
<img src="assets/readme-images/responsive.png">
  <h2>How to play</h2>
  <p>Rock, paper, scissors is a hand game that originated from China, and this app is based on that classic two player game.(More details and history about the game <a href="https://en.wikipedia.org/wiki/Rock_paper_scissors">here</a>.)</p>
  <p>In this version of the hand game, the player is first asked whether they'd like to play the game or not. If they choose to play the game the user can then enter their player name and then they are asked "Rock, Paper, Scissors?". This is where the player must type in one of the three items available to compete against the computer. Depending on the computers choice of 'weapon' the user will gain 1 point for a win, the player that scores 5 points first is the winner!</p>
  <p>The following scenarios are how to score points (1pt for each):</p>
  <ul>
    <li>Rock beats Scissors.</li>
    <li>Paper beats Rock.</li>
    <li>Scissors beat Paper.</li>
  </ul>
  
  <h2>Features</h2>
  <h3>Exisitng Features:</h3>
  <ul>
    <li>Create player name.</li>
      <ul>
        <li>This feature enables the user to create a player name that is used throughout the game.</li>
      </ul>
    <img src="assets/readme-images/player-name.png">
    <li>Play against the computer.</li>
    <li>Scoring System.</li>
    <li>Round result message.</li>
    <li>Computers item choice.</li>
    <ul>
      <li>A scoring system updates the score after every round.</li>
      <li>After each round is complete a message is present displaying the round result.</li>
      <li>Once the player has entered their choice of 'weapon' and hit enter, the computers choice of item is revealed.</li>
    </ul>
    <img src="assets/readme-images/victory-score-example.png">
    <img src="assets/readme-images/defeat-example.png">
    <img src="assets/readme-images/tie-example.png">
    <li>Input validation.</li>
    <ul>
      <li>User must enter a valid response, for when starting game and when choosing a 'weapon'.</li>
      <li>If user uses an invalid response, the programme displays an error message containg what the problem is.</li>
    </ul>
    <em>(Invalid start response & error message.)</em>
    <img src="assets/readme-images/invalid-start-example.png"><br>
    <em>(Invalid item choice response & error message.)</em>
    <img src="assets/readme-images/invalid-item-choice.png">
    <li></li>
  </ul>
