# Poker Game

<br>

<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;This project simulates the Texas Hold'em Poker game against up to seven computer players with different personalities. The rules of the game are worked out in detail so that it provides a satisfying experience.</p>
<p align="justify">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>Disclaimer:</i> This was my first programming project, so the code does not meet expected standards.</p>
<br>


## Project presentation

<br>
<p align="center"><img src="images%20for%20GitHub/poker%20game.png" width="720px"></p>
<br>


## Run the project on Windows

<br>

<b>Step 1.</b>&nbsp;&nbsp;Clone the repository:
<pre>
cd %HOMEPATH%

git clone https://github.com/Doc1996/poker-game
</pre>
<br>

<b>Step 2.</b>&nbsp;&nbsp;Create the virtual environment and install dependencies:
<pre>
cd %HOMEPATH%\poker-game

python -m pip install --upgrade pip
python -m pip install --user virtualenv

python -m venv python-virtual-environment
.\python-virtual-environment\Scripts\activate

.\WINDOWS_INSTALLING_PACKAGES.bat
</pre>
<br>

<b>Step 3.</b>&nbsp;&nbsp;Run the program:
<pre>
cd %HOMEPATH%\poker-game

.\python-virtual-environment\Scripts\activate

.\WINDOWS_POKER_GAME_APPLICATION.bat
</pre>
<br>


## Run the project on Linux

<br>

<b>Step 1.</b>&nbsp;&nbsp;Clone the repository:
<pre>
cd $HOME

git clone https://github.com/Doc1996/poker-game
</pre>
<br>

<b>Step 2.</b>&nbsp;&nbsp;Create the virtual environment and install dependencies:
<pre>
cd $HOME/poker-game

python3 -m pip install --upgrade pip
python3 -m pip install --user virtualenv

python3 -m venv python-virtual-environment
source python-virtual-environment/bin/activate

source LINUX_INSTALLING_PACKAGES.sh
</pre>
<br>

<b>Step 3.</b>&nbsp;&nbsp;Run the program:
<pre>
cd $HOME/poker-game

source python-virtual-environment/bin/activate

source LINUX_POKER_GAME_APPLICATION.sh
</pre>
<br>