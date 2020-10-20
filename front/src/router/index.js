import Vue from 'vue';
import VueRouter from 'vue-router';
Vue.use(VueRouter);

const routes = [
	{
		path: '/test',
		name: 'test',
		component: () => import('@/views/Test.vue'),
	},
	{
		path: '/calendar',
		name: 'calendar',
		component: () => import('@/views/calendar.vue'),
	},
];

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes,
});

export default router;
