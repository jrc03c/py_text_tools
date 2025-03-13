import re

alphanumeric = re.compile("[A-Za-z0-9]")


def camelify(x):
    assert type(x) is str, (
        "The value passed into the `camelify` function must be a string!"
    )

    x = x.strip()
    out = ""
    should_capitalize_next_character = False

    for i in range(0, len(x)):
        char = x[i]

        if alphanumeric.match(char) is not None:
            if len(out) == 0:
                out += char.lower()

            elif should_capitalize_next_character:
                out += char.upper()

            else:
                out += char

            should_capitalize_next_character = False

        elif "'" not in char and "’" not in char and "❜" not in char:
            should_capitalize_next_character = True

    return out


# function camelify(text) {
#   if (typeof text !== "string") {
#     throw new Error("`text` must be a string!")
#   }

#   text = text.trim()
#   let out = ""
#   let shouldCapitalizeNextCharacter = false

#   for (let i = 0; i < text.length; i++) {
#     const char = text[i]

#     if (char.match(/[A-Za-z0-9]/g)) {
#       if (out.length === 0) {
#         out += char.toLowerCase()
#       } else if (shouldCapitalizeNextCharacter) {
#         out += char.toUpperCase()
#       } else {
#         out += char
#       }

#       shouldCapitalizeNextCharacter = false
#     } else if (
#       !char.includes("'") &&
#       !char.includes("’") &&
#       !char.includes("❜")
#     ) {
#       shouldCapitalizeNextCharacter = true
#     }
#   }

#   return out
# }

# export { camelify }
