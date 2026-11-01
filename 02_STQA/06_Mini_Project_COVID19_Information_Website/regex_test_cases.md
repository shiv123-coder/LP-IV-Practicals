# Regular Expression Test Cases

These cases match the validation implemented in `register.php` and `index.php`. Run them through the website forms to confirm the actual server-side result.

## 1. Name validation
Pattern: `/^[\p{L}][\p{L}\s.'-]{1,59}$/u`

| Input | Expected | Reason |
|---|---|---|
| `Shivshankar Mali` | Valid | Letters and a space |
| `Mary-Jane` | Valid | Hyphen allowed |
| `O'Neil` | Valid | Apostrophe allowed |
| `A` | Invalid | Fewer than 2 characters |
| `John123` | Invalid | Digits are not allowed |
| `John@Doe` | Invalid | `@` is not allowed |

## 2. Email validation
Pattern: `/^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/`

| Input | Expected |
|---|---|
| `shivshankar@example.com` | Valid |
| `first.last+test@example.co.in` | Valid |
| `not-an-email` | Invalid |
| `name@localhost` | Invalid |
| `name@example.c` | Invalid |

## 3. Password validation
Pattern: `/^(?=.*[A-Za-z])(?=.*\d).{8,72}$/`

| Input | Expected | Reason |
|---|---|---|
| `Project123` | Valid | 8+ chars, letter and digit |
| `password1` | Valid | 8+ chars, letter and digit |
| `short1` | Invalid | Too short |
| `onlyletters` | Invalid | No digit |
| `12345678` | Invalid | No letter |

## 4. Comment validation
Pattern: `/^[\p{L}\p{N}\s.,!?;:'"()\-]{3,1000}$/u`

| Input | Expected |
|---|---|
| `Thank you for the information.` | Valid |
| `Please update this page!` | Valid |
| `Hi` | Invalid (too short) |
| `Hello <script>` | Invalid (angle brackets not permitted) |
| 1001-character comment | Invalid |

## How to test
1. Register using each input in the relevant row.
2. Note whether the site accepts it or displays a validation message.
3. Test comments after signing in.
4. Record the actual results in the mini-project report. Client-side HTML validation improves usability, while PHP validation is authoritative.
