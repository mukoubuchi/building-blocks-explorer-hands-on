# フィードバック

所要時間は約 1 分です。まとめの 5 分に含まれます。フォームは送信用の文章を作るだけで、自動送信しません。講師が指定した共有先へ、内容を確認して貼り付けてください。

<form class="feedback-form" data-feedback-form data-feedback-lang="ja">
<label for="answer-0">理解度</label>
<select id="answer-0" name="理解度" required>
<option value="">選択してください</option>
<option value="説明できる">説明できる</option>
<option value="もう少し練習したい">もう少し練習したい</option>
<option value="支援が必要">支援が必要</option>
</select>
<label for="answer-1">進む速さ</label>
<select id="answer-1" name="進む速さ" required>
<option value="">選択してください</option>
<option value="ちょうどよい">ちょうどよい</option>
<option value="速い">速い</option>
<option value="遅い">遅い</option>
</select>
<label for="answer-2">完了したこと</label>
<select id="answer-2" name="完了したこと" required>
<option value="">選択してください</option>
<option value="必須 2 題">必須 2 題</option>
<option value="必須 2 題と追加課題">必須 2 題と追加課題</option>
<option value="一部のみ">一部のみ</option>
<option value="代替演習">代替演習</option>
</select>
<label for="comments">困った点や改善案（任意）</label>
<textarea id="comments" name="困った点や改善案（任意）" rows="3"></textarea>
<div class="feedback-actions"><button type="submit">共有する文章を作る</button><p data-feedback-status aria-live="polite"></p></div>
<section class="feedback-section feedback-copy-panel" data-feedback-copy-panel hidden>
<textarea data-feedback-output rows="12" readonly aria-label="共有する文章"></textarea>
<button type="button" data-feedback-copy>コピー</button><p data-feedback-copy-status aria-live="polite"></p>
</section>
</form>
