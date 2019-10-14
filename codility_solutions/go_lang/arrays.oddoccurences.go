package solution

// import "fmt"

func Solution(A []int) int {
    
    var m map[int]int
    m = map[int]int{}
    
    for _, i := range A {
        _, exists := m[i]
//        fmt.Println(i)
        if exists ==true {
            delete(m, i)
        } else {
            m[i] = 1
        }
    }
    return_int := 7
// iterate through keys
    for k, _ := range m {
        return_int = k
    }
//    fmt.Println("test",return_int)
    return return_int
}