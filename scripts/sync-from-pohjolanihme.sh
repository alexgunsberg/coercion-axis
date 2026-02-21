#!/usr/bin/env bash
set -euo pipefail

SRC_DEFAULT="/Users/alexgunsberg/Library/CloudStorage/ProtonDrive-alex.gunsberg@proton.me-folder/pohjolanihme_website_v01/layouts/tool/quiz.html"
SRC="${1:-$SRC_DEFAULT}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
DST="$REPO_ROOT/index.html"

if [[ ! -f "$SRC" ]]; then
  echo "Source quiz file not found: $SRC" >&2
  exit 1
fi

awk '/^const allQuestions = \[/,/^const shortIndices = /{print; if ($0 ~ /^const shortIndices = /) exit}' "$SRC" > /tmp/coercion_axis_questions_block.js

awk -v repl=/tmp/coercion_axis_questions_block.js '
BEGIN { while ((getline l < repl) > 0) r = r l ORS }
{
  if (skip) {
    if ($0 ~ /^const shortIndices = /) { skip = 0; next }
    next
  }
  if ($0 ~ /^const allQuestions = \[/) { printf "%s", r; skip = 1; next }
  print
}
' "$DST" > /tmp/coercion_axis_index_step1.html

mv /tmp/coercion_axis_index_step1.html "$DST"
rm -f /tmp/coercion_axis_questions_block.js

echo "Synced question bank + shortIndices from: $SRC"
