# const indent = require("./indent.js")

# test("tests that indentation works as expected", () => {
#   const a = "Hello, world!"
#   const bTrue = "    Hello, world!"
#   const bPred = indent(a, "    ")
#   expect(bPred).toBe(bTrue)

#   const c = "Hello, world!"
#   const dTrue = "\t\t\t\tHello, world!"
#   const dPred = indent(c, "\t\t\t\t")
#   expect(dPred).toBe(dTrue)

#   const e = [
#     "  Hello, world!",
#     "\t\t  My name is Josh!",
#     "    \t\t  What's your name?",
#   ].join("\n")

#   const fTrue = e
#     .split("\n")
#     .map(line => "!!!!!!" + line)
#     .join("\n")

#   const fPred = indent(e, "!!!!!!")
#   expect(fPred).toBe(fTrue)

#   const g = `
#     *question: What's your name?
#       Alice
#       Bob
#       Charlie
#       Denise
#       Something else...
#   `

#   const hTrue = g
#     .split("\n")
#     .map(line => {
#       if (line.trim().length > 0) {
#         return "\t\t" + line
#       } else {
#         return line
#       }
#     })
#     .join("\n")

#   const hPred = indent(g, "\t\t")
#   expect(hPred).toBe(hTrue)
# })
