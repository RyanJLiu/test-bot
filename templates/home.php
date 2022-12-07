<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>使用者作息設定</title>
    <script src="https://static.line-scdn.net/liff/edge/2/sdk.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.0.0/jquery.min.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
</head>
<body>
    <?php

    # 設定資料庫參數
    $hostname= "us-cdbr-east-05.cleardb.net";
    $username= "bb92b47b5b40af";
    $password= "ad501df8";
    $database= "heroku_c420746d6bd4d14";

    # 建立SQL連線
    $link = mysqli_connect( $hostname , $username , $password );
    mysqli_query($link,  "SET NAMES 'UTF8'");
    mysqli_select_db($link, $database) or die("無法選擇資料庫");
    $id="Ud0b3296f8e4a70520b4ed2f2d1b3bdd8";
    $sql = "SELECT * FROM user where 帳號 = '$id'";
    $result = mysqli_query($link, $sql) or die("無法送出" . mysqli_error());
    $content = mysqli_fetch_assoc($result);
    $breakfast = $content['早餐'];
    $lunch = $content['午餐'];
    $dinner = $content['晚餐'];
    $sleep = $content['睡眠'];
    ?>
    <form method="get">
        <div class="row" style="margin: 10px">
            <div class="col-12" style="margin: 10px">
                
                <label>早餐</label>
                <input type="time" id="breakfast" name="breakfast" step="300" value="<?php echo $breakfast?>" class="form-control">
                <br />
                <label>午餐</label>
                <input type="time" id="lunch" name="lunch" step="300" value="<?php echo $lunch?>" class="form-control">
                <br />
                <label>晚餐</label>
                <input type="time" id="dinner" name="dinner"step="300" value="<?php echo $dinner?>" class="form-control">
                <br />
                <label>睡眠</label>
                <input type="time" id="sleep" name="sleep" step="300" value="<?php echo $sleep?>" class="form-control">
                <br />
                <button class="btn btn-warning btn-block" id="sure">確定</button>
            </div>
        </div>
    </form>
</body>
<script>
	function pushMsg(nbr, nlu, ndi, nsl) {
		if (nbr == '' || nlu == '' || ndi == '' || nsl ==' ') {  //資料檢查
			alert('每個時段都要有值！');
			return;
		}
        <?php
        $nbr=$_GET['breakfast'];
        $nlu=$_GET['lunch'];
        $ndi=$_GET['dinner'];
        $nsl=$_GET['sleep'];
        $sqlsetb = "UPDATE user SET 早餐='$nbr' WHERE 帳號 = '$id'";
        $sqlsetl = "UPDATE user SET 午餐='$nlu' WHERE 帳號 = '$id'";
        $sqlsetn = "UPDATE user SET 晚餐='$ndi' WHERE 帳號 = '$id'";
        $sqlsets = "UPDATE user SET 睡眠='$nsl' WHERE 帳號 = '$id'";
        mysqli_query($link, $sqlsetb);
        mysqli_query($link, $sqlsetl);
        mysqli_query($link, $sqlsetn);
        mysqli_query($link, $sqlsets);
        ?>
		var msg = "已更改設定時間:\n";  //回傳訊息字串
		msg = msg + "早餐: " + nbr + "\n";
        msg = msg + "午餐: " + nlu + "\n";
        msg = msg + "晚餐: " + ndi + "\n";
        msg = msg + "睡眠: " + nsl;
		liff.sendMessages([  //推播訊息
			{ type: 'text',
			  text: msg
			}
		])
			.then(() => {
				liff.closeWindow();  //關閉視窗
			});
	}

	liffId="1657681037-2zmOZl30";
	liff.init({liffId
    }).catch(function(error) {
    console.log(error);
    }); //liff.init

    liff.getProfile()
    .then((profile) => {
    const Userid = profile.userId;
    console.log(Userid);
    }).catch((err) => {
    console.log("error", err);
    });
		
	$('#sure').click(function (e) {  //按下確定鈕
		pushMsg($('#breakfast').val(), $('#lunch').val(), $('#dinner').val(), $('#sleep').val());
		});
</script>
<?php
mysqli_close($link);
?>
</html>

