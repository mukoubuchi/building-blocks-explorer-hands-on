# Feedback

Allow about one minute, included in the five-minute review. This form composes a message locally; it does not send it. Review the text and paste it into the channel designated by the instructor.

<form class="feedback-form" data-feedback-form data-feedback-lang="en">
<label for="answer-0">Understanding</label>
<select id="answer-0" name="Understanding" required>
<option value="">Select one</option>
<option value="I can explain it">I can explain it</option>
<option value="I need more practice">I need more practice</option>
<option value="I need help">I need help</option>
</select>
<label for="answer-1">Pace</label>
<select id="answer-1" name="Pace" required>
<option value="">Select one</option>
<option value="Just right">Just right</option>
<option value="Too fast">Too fast</option>
<option value="Too slow">Too slow</option>
</select>
<label for="answer-2">Completion</label>
<select id="answer-2" name="Completion" required>
<option value="">Select one</option>
<option value="Both required exercises">Both required exercises</option>
<option value="Both required and optional">Both required and optional</option>
<option value="Partial completion">Partial completion</option>
<option value="Fallback exercise">Fallback exercise</option>
</select>
<label for="comments">Blockers or suggestions (optional)</label>
<textarea id="comments" name="Blockers or suggestions (optional)" rows="3"></textarea>
<div class="feedback-actions"><button type="submit">Prepare feedback message</button><p data-feedback-status aria-live="polite"></p></div>
<section class="feedback-section feedback-copy-panel" data-feedback-copy-panel hidden>
<textarea data-feedback-output rows="12" readonly aria-label="Feedback message"></textarea>
<button type="button" data-feedback-copy>Copy</button><p data-feedback-copy-status aria-live="polite"></p>
</section>
</form>
