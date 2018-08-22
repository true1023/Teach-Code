var comp1 = {
    data: function () {
        return {
          count: 0
        }
      },
      template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
}
/*
// 定义一个名为 button-counter 的新组件
Vue.component('button-counter', {
    data: function () {
      return {
        count: 0
      }
    },
    template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
})
Vue.component('temp1', {
    data: function () {
      return {
        count: 0
      }
    },
    template: '<h1>Temp1</h1>'
 })
Vue.component('temp2', {
    data: function () {
      return {
        count: 0
      }
    },
    template: '<h1>Temp2</h1>'
})
Vue.component('temp3', {
    data: function () {
      return {
        count: 0
      }
    },
    template: '<h1>Temp3</h1>'
})
*/