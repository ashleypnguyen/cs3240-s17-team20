<?php
require "dbutil.php";
$db = DbUtil::loginConnection();

$stmt = $db->stmt_init();

if($stmt->prepare("select * from Sailors where sname like ?") or die(mysqli_error($db))) {
  $searchString = '%' . $_GET['searchName'] . '%';
  $stmt->bind_param(s, $searchString);
  $stmt->execute();
  $stmt->bind_result($sid, $sname, $rating, $age);
  echo "<table border=1><th>sid</th><th>sname</th><th>rating</th><th>age</th>\n";
  while($stmt->fetch()) {
    echo "<tr><td>$sid</td><td>$sname</td><td>$rating</td><td>$age</td></tr>";
  }
  echo "</table>";

  $stmt->close();
}

$db->close();


?>
