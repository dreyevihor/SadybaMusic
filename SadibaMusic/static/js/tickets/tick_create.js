vm1 = new Vue({
    el: "#evnt",
    data: {
        check_event: '',
        events: [],
    },
    created: function(){
        var self = this
        axios.get('/api/events/').then(function(response) {
            self.events = response.data
            console.log(response.data)
          })
    },
    watch: {
        check_event: function(){
            vm3.event = this.check_event
        } 
    },
    delimiters: ["[[","]]"]
});
vm2 = new Vue({
    el: "#halls",
    data: {
        check_hall: 0,
        halls: [],
    },
    created: function(){
        var self = this
        axios.get('/api/halls/').then(function(response) {
            self.halls = response.data
          })
    },
    watch:{
        check_hall: function(){
            vm3.hall = this.check_hall
        } 
    },
    delimiters: ["[[","]]"]
});


vm3 = new Vue({
    el: "#send",
    data: {
        event: 0,
        hall: 0,
        token: ''
       },


       methods: {
            submit: function(){
                this.token = Cookies.get('csrftoken');
                headers = {"X-CSRFToken": this.token};
                axios.post('/tickets/create/', {
                            'event': this.event,
                            'hall': this.hall
                             }, {headers: headers}).then(function(response) {
                                window.location.href = response.request.responseURL;
                                              })

            }
       },
    


});
