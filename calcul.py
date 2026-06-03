
<script type="mpy">
            from pyscript import display

            def wallis(n):
                pi = 2
                for i in range(1, n):
                    pi *= 4 * i ** 2 / (4 * i ** 2 - 1)
                return pi

            def jugador_p(event):
                pi = wallis(100000)
                s = f"π es aproximadament {pi:.3f}"
                display(s, target="pi", append=False)  
        </script>