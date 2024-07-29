<?php
function cpu(){
	$loads=sys_getloadavg();
	$core_nums=trim(shell_exec("grep -P '^physical id' /proc/cpuinfo|wc -l"));
	$load=($loads[0]/$core_nums) * 100;
	return number_format($load,2);
}

function ram_usage(){
	$memTotal = 0;
    $memAvailable = 0;
    
    $fh = fopen('/proc/meminfo', 'r');
    while ($line = fgets($fh)) {
        $pieces = array();
        if (preg_match('/^MemTotal:\s+(\d+)\skB$/', $line, $pieces)) {
            $memTotal = $pieces[1];
        }
        if (preg_match('/^MemAvailable:\s+(\d+)\skB$/', $line, $pieces)) {
            $memAvailable = $pieces[1];
        }
        if ($memTotal && $memAvailable) {
            break;
        }
    }
    fclose($fh);
	$memUsed = $memTotal - $memAvailable;
    	$ramUsage = ($memUsed / $memTotal) * 100;
	return number_format($ramUsage, 2);
}

if(isset($_GET['load'])){
	echo cpu();
	exit;
}

if(isset($_GET['memory'])){
	echo ram_usage();
	exit;
}

$neofetch = shell_exec('neofetch --stdout');
echo "<pre> " . $neofetch . "</pre>";

$procesy = array("apache2","vsftpd","pihole-FTL");
foreach($procesy as $proces){
	if(trim(shell_exec("systemctl is-active $proces"))){
		echo "$proces is active <br>";
	}
	else{
		echo "$proces is down <br>";
	}

}

echo "free " . number_format(disk_free_space("/") / 1073741824, 0) . "GB out of " . number_format(disk_total_space("/") / 1073741824, 0);

?>
<!DOCTYPE html>
<html lang="pl">
<head>
	<meta charset="UTF-8">
	<script>
		function get_cpu(){
			var xhr = new XMLHttpRequest();

			xhr.open('GET', 'system_info.php?load', true);
			xhr.onload = function(){
				document.getElementById("cpu_status").innerText = xhr.responseText;
			};
			xhr.send();
		}

		function get_ram(){
			var xhr = new XMLHttpRequest();
			xhr.open('GET', 'system_info.php?memory', true);
			xhr.onload = function(){ document.getElementById("ram_status").innerText = xhr.responseText;}
			xhr.send();			
		}
		
		document.addEventListener("DOMContentLoaded", function(){
			get_cpu();
			get_ram();
			setInterval(get_ram, 1000);
			setInterval(get_cpu, 1000);}
);
		
	</script>
</head>
<body>
	<p> cpu usage: <span id="cpu_status">dupa</span> %</p>
	<p> ram usage: <span id="ram_status">test</span> %</p>	
</body>
</html>
