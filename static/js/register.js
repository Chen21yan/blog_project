$(function(){
    function bindCaptchaBtnClick(){
        $("#captcha-btn").click(function(event){
            let $this = $(this);
            let email = $("input[name='email']").val()
            if(!email){
                alert("请先输入邮箱！");
                return;
            }
            // 取消按钮的点击事件
            $this.off('click');
            // 倒计时
            let countdown = 6;
            let timer = setInterval(function(){
                if(countdown<=0){
                    $this.text("获取验证码");
                    // 清掉定时器
                    clearInterval(timer);
                    // 重新绑定点击事件
                    bindCaptchaBtnClick();
                }else{
                    countdown--;
                    $this.text(countdown+"s")
                }
            },1000);
        })
    }
    bindCaptchaBtnClick();
});