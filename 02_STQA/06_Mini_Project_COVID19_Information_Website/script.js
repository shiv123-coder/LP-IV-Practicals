document.addEventListener('DOMContentLoaded', () => {
  const comment = document.getElementById('comment');
  const count = document.getElementById('commentCount');
  if (comment && count) {
    const updateCount = () => {
      count.textContent = `${comment.value.length} / 1000 characters`;
      count.style.color = comment.value.length > 1000 ? '#b42318' : '';
    };
    comment.addEventListener('input', updateCount);
    updateCount();
  }
});
