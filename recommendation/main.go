package main

import (
    "encoding/json"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    data := map[string]string{"recommendation": "Watch 'Ex Machina'"}
    json.NewEncoder(w).Encode(data)
}

func main() {
    http.HandleFunc("/recommendation", handler)
    http.ListenAndServe(":8082", nil)
}