<!doctype html>

<title>checkin.py</title>

<style>
body {
  width: 700px;
  margin: auto;
}
.msg { 
  padding: 10px 15px;
  border: 1px solid #aaa;
  text-align: center;
  color: #555;
  background-color: #fafafa;
}

form {
  text-align: center;
}
input[type="submit"] {
  font-size: 200%;
  padding: 10px 50px;
}

h1 {
  margin-top: 50px;
}
</style>


% if current_checkin:
  <p class=msg>You checked in at {{ current_checkin['checkin'].strftime('%H:%M') }}</p>
% elif checked_out_after:
  <p class=msg>You checked out after {{ '%.1f' % checked_out_after }} hours of work</p>
% else:
  <p class=msg>Not checked in</p>
% end


<form method=POST action="">
  <input type=submit
    % if current_checkin:
      value="Check out"
    % else:
      value="Check in"
    % end
  />
</form>


<h1>Balance: {{ '%+.1f' % (have_worked - should_have_worked) }} hours</h1>

<h1>All attendances</h1>
<ul>
% for attendance in past_attendances:
  % if not defined('_month') or get('_month') != attendance['checkin'].month:
    % setdefault('_month', attendance['checkin'].month)
    </ul>
    <h2>{{ attendance['checkin'].strftime('%B') }}</h2>
    <ul>
  % end
  <li>{{ attendance['delta'] }} on {{ attendance['checkin'].strftime('%A %B %d %Y') }}</li>
% end
</ul>
