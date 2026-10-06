<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>2210 전승민 - 오목 게임</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>

    <div class="container">

        <header>
            <h1>⚫ 2210 전승민 오목 게임 ⚪</h1>
            <p>흑돌과 백돌을 번갈아 놓아 5개를 먼저 연결하세요!</p>
        </header>

        <div class="game-info">
            <div id="turn">현재 차례: ⚫ 흑돌</div>
            <div id="message">게임을 시작하세요!</div>
        </div>

        <div class="board-container">
            <div id="board"></div>
        </div>

        <button id="restartButton">🔄 게임 다시 시작</button>

        <div class="rules">
            <h2>🎮 게임 방법</h2>
            <ul>
                <li>흑돌부터 게임을 시작합니다.</li>
                <li>흑돌과 백돌을 번갈아 놓습니다.</li>
                <li>가로, 세로, 대각선 중 하나로 돌 5개를 연결하면 승리합니다.</li>
                <li>게임이 끝난 후 다시 시작 버튼을 누르면 새 게임을 시작할 수 있습니다.</li>
            </ul>
        </div>

        <footer>
            <p>2210 전승민 제작</p>
        </footer>

    </div>

    <script src="script.js"></script>

</body>
</html>
