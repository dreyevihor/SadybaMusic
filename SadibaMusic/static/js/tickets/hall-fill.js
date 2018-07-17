vm1 = new Vue({
    el: "#app",
    data: {
        rows: [],
    },
    created: function(){
        var vm = this;
        var hall_id = window.location.toString().split('/fillPrice/')[1]
        axios.get('/api/halls/' + hall_id)
            .then(function(response){
                var data = response.data.rows
                data.forEach(element => {
                    element.price = '';                    
                });
                function sortByNum(rowA, rowB){
                    return rowA['number'] - rowB['number'];
                }
                vm.rows = data.sort(sortByNum)
        });
    },
    methods: {
        addRow: function(){
            this.rows.push({
                number: 0,
                place_from: 0,
                place_to: 0,
                price: 0,
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
        token: '',

       },
    created: function(){
        this.token = Cookies.get('csrftoken');   
    },
       methods: {
            submit: function(){
                this.token = Cookies.get('csrftoken');
                headers = {"X-CSRFToken": this.token};
                axios.post(window.location.toString(), {
                            'rows': vm1.rows,
                     }, {headers: headers}).then(function(response) {
                        window.location.href = response.request.responseURL;
                                              })

            }
       },
    });