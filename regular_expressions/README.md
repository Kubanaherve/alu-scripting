# Regular Expressions

Ruby scripts using Oniguruma regular expressions. Each script takes one
argument and prints all matches using `scan`/`join`.

| File | Pattern | Description |
|---|---|---|
| `0-simply_match_school.rb` | `/School/` | Matches `School` |
| `1-repetition_token_0.rb` | `/hbt{2,5}n/` | `h` + `b` + 2-5 `t`s + `n` |
| `2-repetition_token_1.rb` | `/hb?tn/` | `h` + optional `b` + `t` + `n` |
| `3-repetition_token_2.rb` | `/hbt+n/` | `h` + `b` + 1 or more `t`s + `n` |
| `4-repetition_token_3.rb` | `/hbt*n/` | `h` + `b` + 0 or more `t`s + `n` (no `[]`) |
| `5-beginning_and_end.rb` | `/^h.n$/` | Starts with `h`, ends with `n`, one char in between |
| `6-phone_number.rb` | `/^\d{10}$/` | Exactly 10 digits |
| `7-OMG_WHY_ARE_YOU_SHOUTING.rb` | `/[A-Z]/` | Only capital letters |
| `8-textme.rb` | `\[from:(.*?)\]` etc. | Outputs `SENDER,RECEIVER,FLAGS` from TextMe log |
| `9-passed_linkedin_regex_challenge.jpg` | — | Screenshot of LinkedIn regex puzzle (manual step, not yet completed) |

All `.rb` files use `#!/usr/bin/env ruby`, are executable, and end with a newline.
