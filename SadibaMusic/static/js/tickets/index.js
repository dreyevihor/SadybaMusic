vm1 = new Vue({
    el: "#download",
    data: {
        file: ''        
    },
    watch:{
        file: function(){
            window.location.href ='http://127.0.0.1:8000' + this.file
        }
    },
    delimiters: ["[[","]]"]
});