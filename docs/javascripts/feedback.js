(function () {
  var MESSAGES = {
    ja: {
      header: 'Building Blocks Explorer ハンズオン フィードバック',
      divider: '━━━━━━━━━━━━━━━━━━━━',
      noAnswer: '未回答',
      status: '共有する文章を作成しました。',
      copySuccess: 'コピーしました。講師が指定した共有先へ貼り付けてください。',
      copyFailure: 'コピーできませんでした。内容を選択して手動でコピーしてください。'
    },
    en: {
      header: 'Building Blocks Explorer Hands-on Feedback',
      divider: '━━━━━━━━━━━━━━━━━━━━',
      noAnswer: 'No answer',
      status: 'Created your feedback message.',
      copySuccess: 'Copied. Paste it into the channel designated by your instructor.',
      copyFailure: 'Copy failed. Please select the content and copy it manually.'
    }
  };

  function collectFormData(form, messages) {
    var entries = [];
    var fields = form.querySelectorAll('select, textarea');

    fields.forEach(function (field) {
      if (field.hasAttribute('data-feedback-output')) {
        return;
      }

      var label = field.name || field.id;
      var value = (field.value || '').trim();
      entries.push('■ ' + label + '\n' + (value || messages.noAnswer));
    });

    return entries.join('\n\n');
  }

  function copyText(textarea, status, messages) {
    var text = textarea.value;

    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () {
        if (status) {
          status.textContent = messages.copySuccess;
        }
      }).catch(function () {
        textarea.focus();
        textarea.select();

        if (status) {
          status.textContent = messages.copyFailure;
        }
      });
      return;
    }

    textarea.focus();
    textarea.select();

    try {
      document.execCommand('copy');
      if (status) {
        status.textContent = messages.copySuccess;
      }
    } catch (error) {
      if (status) {
        status.textContent = messages.copyFailure;
      }
    }
  }

  function handleFeedbackSubmit(event) {
    event.preventDefault();

    var form = event.currentTarget;
    if (!form.checkValidity()) {
      form.reportValidity();
      return;
    }

    var lang = form.getAttribute('data-feedback-lang');
    var messages = MESSAGES[lang] || MESSAGES.en;
    var body = messages.divider + '\n' + messages.header + '\n' + messages.divider + '\n\n' + collectFormData(form, messages);
    var status = form.querySelector('[data-feedback-status]');
    var panel = form.querySelector('[data-feedback-copy-panel]');
    var output = form.querySelector('[data-feedback-output]');

    if (status) {
      status.textContent = messages.status;
    }

    if (output) {
      output.value = body;
    }

    if (panel) {
      panel.hidden = false;
      panel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('[data-feedback-form]').forEach(function (form) {
      form.addEventListener('submit', handleFeedbackSubmit);

      var lang = form.getAttribute('data-feedback-lang');
      var messages = MESSAGES[lang] || MESSAGES.en;
      var copyButton = form.querySelector('[data-feedback-copy]');
      var output = form.querySelector('[data-feedback-output]');
      var copyStatus = form.querySelector('[data-feedback-copy-status]');

      if (copyButton && output) {
        copyButton.addEventListener('click', function () {
          copyText(output, copyStatus, messages);
        });
      }
    });
  });
}());
