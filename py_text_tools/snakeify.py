# const strip = require("./helpers/strip.js")

# function snakeify(text) {
#   if (typeof text !== "string") {
#     throw new Error("`text` must be a string!")
#   }

#   const words = strip(text).split(" ")

#   if (words.length === 0) return ""
#   if (words.length === 1) return words[0]

#   return words.join("_")
# }
