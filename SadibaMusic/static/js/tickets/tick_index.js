vm1 = new Vue({
    el: "#app",
    data: {
        rows: [],
    },
    methods: {
        addRow: function(){
            this.rows.push({
                row_from: 0,
                row_to: 0,
                place_from: 0,
                place_to: 0,
            })
        },
        removeRow: function(i){
            this.rows.splice(i, 1)
        }

    },
    watch: {
        rows: function(){
            vm2.rows = this.rows
        }
    },
    delimiters: ["[[","]]"]
});

vm2 = new Vue({
    el: "#send",
    data: {
        rows: [],
        title: '',
        token: '',

       },


       methods: {
            submit: function(){
                this.token = Cookies.get('csrftoken');
                headers = {"X-CSRFToken": this.token};
                axios.post('/halls/create/', {
                            'rows': this.rows,
                            'title': this.title
                             }, {headers: headers}).then(function(response) {
                                                // handle success
        
                                                window.location.href = response.request.responseURL;
                                              })

            }
       },
    


});

vm3 = new Vue({
    el: "#name",
    data: {
        title: ''
    },
    watch:{
        title: function(){
            vm2.title = this.title
        }
    }
})