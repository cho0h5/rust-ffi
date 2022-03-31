# C
gcc main.c -lwasm_deno_example -L./target/debug -o main
export LD_LIBRARY_PATH=./target/debug:$LD_LIBRARY_PATH
