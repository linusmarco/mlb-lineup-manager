<template>
    <footer id="site-footer">
        <div id="copyright">
            <span>
                Built at Baseball Hackday 2019
            </span>
        </div>
    </footer>
</template>

<script>
export default {
    name: 'Footer',
    data() {
        return {
            curYr: new Date().getFullYear()
        };
    }
};
</script>

<style scoped>
#site-footer {
    color: black;
    background-color: white;
    border-top: 1px solid grey;
    height: 3rem;
    padding: 0 1rem;
    text-align: center;

    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
}

#copyright {
    height: 2.5rem;
    line-height: 2.5rem;
    font-size: 1rem;
}
</style>
