const { url } = require("inspector");

const app = Vue.createApp({
    methods: {
        getThanks() {
            axios.get('http://127.0.0.1:8000/api/thankyou')
                .then(response => {
                    this.$router.push('/thankyou');
                })

        }
    }
});
app.mount('#app');