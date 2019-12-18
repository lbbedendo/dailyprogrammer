import java.util.stream.IntStream

fun stair(n: Int) {
    IntStream.range(1, n).forEach {
        println(" ".repeat(n - it) + "#".repeat(it))
    }
}

fun main() {
    print("Enter the stair size: ")
    val n = readLine()!!
    stair(n.toInt())
}
