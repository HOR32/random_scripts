declare -A pm;
pm[/etc/arch-release]=pacman
pm[/etc/gentoo-release]=emerge
pm[/etc/SuSE-release]=zypp
pm[/etc/debian_version]=apt
pm[/etc/alpine-release]=apk
for x in ${!pm[@]}
do
	if [[ -f $x ]]; then
		echo ${pm[$x]}
	fi
done
